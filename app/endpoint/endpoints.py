import ast
import datetime
import geocoder
import base64

from ..database import db
from validate_docbr import CPF
from flask import jsonify, request
from sqlalchemy import and_

from ..rotas.jsonRout import json_bp
from ..enum.statusEventoEnum import StatusEventoEnum
from ..models.categoriaModel import Categoria
from ..models.subcategoriaModel import Subcategoria
from ..models.eventoModel import Evento
from ..models.eventoHistoricoModel import EventoHistorico
from app.models.eventoObservacaoModel import EventoObservacao
from ..models.userModel import User
from ..models.statusEventoModel import StatusEvento
from ..serializable import categoriaSchema, subcategoriaSchema, statusSchema, eventoHistoricoSchema, userSchema


class endpoint():

    global ROWS_PER_PAGE 
    ROWS_PER_PAGE = 5

    @json_bp.route('/cadastrarEvento' , methods=['POST'])
    def cadastrarEvento():

        try:
            data = request.get_json()

            idSubcategoria = data['idSubcategoria']
            idUsuario = data['idUsuario']
            txtProblema = data['txtProblema']
            txtEndereco = data['txtEndereco']
            txtLat = data['txtLat']
            txtLong = data['txtLong']
            fileBase64 = data['fileBase64']
            dataInicio = datetime.datetime.now()

            if not txtLat and not txtLong:
                g = geocoder.osm(txtEndereco)

                if not g:
                    return jsonify({"Status": "Endereço {} não encontrado".format(txtEndereco)}), 404

                latlong = g.json
                txtLat = latlong['lat']
                txtLong = latlong['lng']

            bytesFile = base64.b64decode(fileBase64)
            numOcorrencia = str(dataInicio.year) + str(idUsuario) + str(dataInicio.day) + str(dataInicio.month) + str(dataInicio.hour) + str(dataInicio.minute) + str(dataInicio.second)

            evento = Evento(idSubcategoria, idUsuario, numOcorrencia, txtProblema, txtEndereco, txtLat, txtLong, bytesFile, dataInicio)
            eventoHistorico= EventoHistorico(evento, StatusEventoEnum.AGUARDANDO_ATENDIMENTO.value, idUsuario, dataInicio)

            db.session.add(eventoHistorico)
            db.session.commit()

            return jsonify({"Status:": "Evento cadastrado com sucesso!"})
        except Exception as e:
            return jsonify({"Status:" : str(e)}), 400

    @json_bp.route('/consultarEvento', methods=["POST"])
    def consultarEvento():
        data = request.get_json()

        if 'numOcorrencia' not in data:
            return jsonify({"Status": "Campo 'numOcorrencia' ausente no JSON"}), 400

        numOcorrencia = data['numOcorrencia']
        eventoHistorico = EventoHistorico.query.filter(and_(EventoHistorico.dataFim.is_(None), EventoHistorico.evento.has(Evento.numOcorrencia == numOcorrencia))).first()

        if eventoHistorico is None:
            return jsonify({"Status": "Ocorrência {} não encontrada".format(numOcorrencia)}), 404

        return eventoHistoricoSchema.evento_historico_schema.dump(eventoHistorico)
    
    @json_bp.route('/cadastrarObservacao/' , methods=['POST'])
    def cadastrarObservacao():

        data = request.get_json()

        idEventoHistorico = data['idEventoHistorico']
        idUsuario = data['idUsuario']
        txtObservacao = data['txtObservacao']
        dataInicio = datetime.datetime.now()

        try:
            eventoObservacao = EventoObservacao(idEventoHistorico, idUsuario, txtObservacao, dataInicio)
            db.session.add(eventoObservacao)
            db.session.commit()

            return jsonify({"Status:": "Observação cadastrado com sucesso!"})
        except Exception as e:
            return jsonify({"Status:" : str(e)}), 400 

    @json_bp.route('/atenderOcorrencia', methods=['GET'])
    def atenderOcorrencia():

        try:

            numOcorrencia = request.args.get('numOcorrencia')
            idUsuario = request.args.get('idUsuario')
            dataInicio = datetime.datetime.now()

            eventoHistorico = db.session.query(EventoHistorico).join(Evento).filter(and_(Evento.numOcorrencia == numOcorrencia, EventoHistorico.dataFim.is_(None))).first()
            eventoHistorico.dataFim = dataInicio
            
            newEventoHistorico = EventoHistorico(eventoHistorico.evento, StatusEventoEnum.EM_ANDAMENTO.value, idUsuario, dataInicio)
            db.session.add(newEventoHistorico)
            db.session.commit()

            return jsonify({"Status:": "Ocorrência em andamento!"})
        except Exception as e:
            db.session.rollback()
            return jsonify({"Status:" : str(e)}), 400

    @json_bp.route('/finalizarOcorrencia', methods=['GET'])
    def finalizarOcorrencia():

        try:
            numOcorrencia = request.args.get('numOcorrencia')
            idUsuario = request.args.get('idUsuario')
            dataInicio = datetime.datetime.now()

            eventoHistorico = db.session.query(EventoHistorico).join(Evento).filter(and_(Evento.numOcorrencia == numOcorrencia, EventoHistorico.dataFim.is_(None))).first()

            if eventoHistorico.idStatusEvento != StatusEventoEnum.EM_ANDAMENTO.value:
                return jsonify({"Status:": "Ocorrência {} não pode ser finalizada. Atenda a ocorrência".format(numOcorrencia)})

            eventoHistorico.dataFim = dataInicio

            newEventoHistorico= EventoHistorico(eventoHistorico.evento, StatusEventoEnum.FINALIZADO.value, idUsuario.id, dataInicio)
            db.session.add(newEventoHistorico)
            db.session.commit()

            return jsonify({"Status:": "Ocorrência finalizada com sucesso!"})
        except Exception as e:
            db.session.rollback()
            return jsonify({"Status:" : str(e)}), 400

    @json_bp.route('/listarEventosPaginado', methods=['GET'])
    def listarEventosPaginado():

        try:
            page = request.args.get('page', 1, type=int)
            
            listHistoricoEvento = EventoHistorico.query.filter(and_(EventoHistorico.idStatusEvento != StatusEventoEnum.FINALIZADO.value, EventoHistorico.dataFim.is_(None))).order_by(EventoHistorico.dataInicio.desc()).paginate(page=page, per_page=ROWS_PER_PAGE)

            if listHistoricoEvento is None:
                return jsonify({"Status": "Nenhuma Ocorrência Encontrada"}), 200
            
            eventos = eventoHistoricoSchema.eventos_historicos_schema.dump(listHistoricoEvento.items)

            return jsonify({"eventos": eventos})

        except Exception as e:
            return jsonify({"Status:" : str(e)}), 400   


    @json_bp.route('/listarTodosEventos', methods=['GET'])
    def listarTodosEventos():

        try:
            
            listHistoricoEvento = EventoHistorico.query.filter(and_(EventoHistorico.idStatusEvento != StatusEventoEnum.FINALIZADO.value, EventoHistorico.dataFim.is_(None))).order_by(EventoHistorico.dataInicio.desc()).all()

            if listHistoricoEvento is None:
                return jsonify({"Status": "Nenhuma Ocorrência Encontrada"}), 200
            
            eventos = eventoHistoricoSchema.eventos_historicos_schema.dump(listHistoricoEvento)

            return jsonify({"eventos": eventos})

        except Exception as e:
            return jsonify({"Status:" : str(e)}), 400
        
    @json_bp.route('/categorias', methods=["GET"])
    def categorias():

        try:
            listCategoria = Categoria.query.filter(Categoria.dataFim.is_(None)).all()

            if listCategoria is None:
                return jsonify({"Status": "Nenhuma Ocorrência Encontrada"}), 200
            
            categoria = categoriaSchema.categoria_schema.dump(listCategoria)

            return jsonify({"categorias": categoria})
        
        except Exception as e:
            return jsonify({"Status:" : str(e)}), 400
        
    @json_bp.route('/subcategoria', methods=["GET"])
    def subcategoria():

        idCategoria = request.args.get('idCategoria')

        if not idCategoria:
            return jsonify({"Status": "Campo 'idCategoria' ausente no JSON"}), 400

        try:
            subcategoria = Subcategoria.query.filter(and_(Subcategoria.dataFim.is_(None), Subcategoria.idCategoria == idCategoria)).first()

            if subcategoria is None:
                return jsonify({"Status": "Nenhuma Ocorrência Encontrada"}), 200
            
            return subcategoriaSchema.subcategoria_schema.dump(subcategoria)
        
        except Exception as e:
            return jsonify({"Status:" : str(e)}), 400 

    @json_bp.route('/logar', methods=['POST'] )
    def logar(): 

        data = request.get_json()

        try:
            email = data['email']
            pwd = data['pwd']

            user = User.query.filter_by(email=email).first()

            if not user or not user.verify_password(pwd):
                return jsonify({"Status": "Usuário ou Senha inválidos"}), 401  

            roles = []
            if user.flgAdmin:
                roles = ['URBANMOB_ADMIN','URBANMOB_GOVERNO']
            elif user.flgGoverno :
                roles = ['URBANMOB_GOVERNO']
            else:
                roles = ['URBANMOB_USER']

            data = {"user": userSchema.user_schema.dump(user), "role":roles}

            return data

        except Exception as e:
            return jsonify({"Status": str(e)}), 400 
            
    @json_bp.route('/registrarUsuario', methods=["POST"])
    def registrarUsuario():

        data = request.get_json()

        nome = data['nome']
        email = data['email']
        cpf = data['cpf']
        senha = data['senha']
        senha_confirmar = data['senha_confirmar']
        flg_admin = data['flg_admin']
        flg_governo = data['flg_governo']

        if not nome:
            return jsonify({"Status": "Campo 'nome' ausente no JSON"}), 400

        if not email:
            return jsonify({"Status": "Campo 'email' ausente no JSON"}), 400

        if not cpf:
            return jsonify({"Status": "Campo 'cpf' ausente no JSON"}), 400

        if not senha:
            return jsonify({"Status": "Campo 'senha' ausente no JSON"}), 400

        if not senha_confirmar:
            return jsonify({"Status": "Campo 'senha_confirmar' ausente no JSON"}), 400

        if senha != senha_confirmar:
            return jsonify({"Status": "As senhas informadas estão divergentes"}), 400

        obj = CPF()
        if not obj.validate(cpf): 
            return jsonify({'Status: {}'.format('Ops. Não nos parece um CPF válido')}), 401

        try:

            user = User(nome, email, cpf, senha, ast.literal_eval(flg_governo), ast.literal_eval(flg_admin))

            db.session.add(user)
            db.session.commit()
            return jsonify({"Status:": "Usuário cadastrado com sucesso!"}) 

        except Exception as e:
            db.session.rollback()
            return jsonify({"Status:" : str(e)}), 400

    @json_bp.route('/status', methods=["GET"])
    def status():

        try:
            listStatus = StatusEvento.query.filter(StatusEvento.dataFim.is_(None)).all()

            if listStatus is None:
                return jsonify({"Status": "Nenhuma Ocorrência de Status Encontrada"}), 200

            status = statusSchema.status_schema.dump(listStatus)

            return jsonify({"status": status})
        
        except Exception as e:
            return jsonify({"Status:" : str(e)}), 400              