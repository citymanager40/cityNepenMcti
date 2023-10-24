from flask_login import login_required
from flask import jsonify, request
from ..models.eventoModel import Evento
from app.models.eventoHistoricoModel import EventoHistorico
from ..rotas.eventoJsonRout import eventoJson_bp
from sqlalchemy import and_
from ..serializable.eventoHistoricoSchema import evento_historico_schema

class eventoJson():

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
