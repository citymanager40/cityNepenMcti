from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.eventoHistoricoModel import EventoHistorico
from ..serializable.eventoSchema import EventoSchema
from ..serializable.statusEventoSchema import StatusEventoSchema

class EventoHistoricoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = EventoHistorico

    evento = fields.Nested(EventoSchema)
    statusEvento = fields.Nested(StatusEventoSchema)
    # statusEvento_id = fields.Integer(attribute="statusEvento.id")
    # usuario_id = fields.Integer(attribute="usuario.id")

evento_historico_schema = EventoHistoricoSchema()
eventos_historicos_schema = EventoHistoricoSchema(many=True)
