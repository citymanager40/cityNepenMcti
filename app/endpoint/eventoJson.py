from flask_login import login_required
from flask import jsonify, request
from app.enum.statusEventoEnum import StatusEventoEnum
from ..models.eventoModel import Evento
from app.models.eventoHistoricoModel import EventoHistorico
from ..rotas.eventoJsonRout import eventoJson_bp
from sqlalchemy import and_
from ..serializable.eventoHistoricoSchema import evento_historico_schema, eventos_historicos_schema

class eventoJson():

    global ROWS_PER_PAGE 
    ROWS_PER_PAGE = 5

    @eventoJson_bp.route('/consultarEvento', methods=["POST"])
    # @login_required
    def consultarEvento():
        data = request.get_json()

        if 'numOcorrencia' not in data:
            return jsonify({"Status": "Campo 'numOcorrencia' ausente no JSON"}), 400

        numOcorrencia = data['numOcorrencia']
        eventoHistorico = EventoHistorico.query.filter(and_(EventoHistorico.dataFim.is_(None), EventoHistorico.evento.has(Evento.numOcorrencia == numOcorrencia))).first()

        if eventoHistorico is None:
            return jsonify({"Status": "Ocorrência {} não encontrada".format(numOcorrencia)}), 404

        return evento_historico_schema.dump(eventoHistorico)
    
    @eventoJson_bp.route('/listarEventosPaginado', methods=['GET'])
    # @login_required
    def listarEventosPaginado():

        try:
            page = request.args.get('page', 1, type=int)
            
            listHistoricoEvento = EventoHistorico.query.filter(and_(EventoHistorico.idStatusEvento != StatusEventoEnum.FINALIZADO.value, EventoHistorico.dataFim.is_(None))).order_by(EventoHistorico.dataInicio.desc()).paginate(page=page, per_page=ROWS_PER_PAGE)

            if listHistoricoEvento is None:
                return jsonify({"Status": "Nenhuma Ocorrência Encontrada"}), 200
            
            eventos = eventos_historicos_schema.dump(listHistoricoEvento.items)

            return jsonify({"eventos": eventos})

        except Exception as e:
            return jsonify({"Status:" : str(e)}), 400   


    @eventoJson_bp.route('/listarTodosEventos', methods=['GET'])
    # @login_required
    def listarTodosEventos():

        try:
            
            listHistoricoEvento = EventoHistorico.query.filter(and_(EventoHistorico.idStatusEvento != StatusEventoEnum.FINALIZADO.value, EventoHistorico.dataFim.is_(None))).order_by(EventoHistorico.dataInicio.desc()).all()

            if listHistoricoEvento is None:
                return jsonify({"Status": "Nenhuma Ocorrência Encontrada"}), 200
            
            eventos = eventos_historicos_schema.dump(listHistoricoEvento)

            return jsonify({"eventos": eventos})

        except Exception as e:
            return jsonify({"Status:" : str(e)}), 400 