from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.eventoHistoricoModel import EventoHistorico
from  ..serializable.eventoSchema import EventoSchema
from base64 import b64encode

class EventoHistoricoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = EventoHistorico

    evento = fields.Nested(EventoSchema)
    statusEvento_id = fields.Integer(attribute="statusEvento.id")
    usuario_id = fields.Integer(attribute="usuario.id")

evento_historico_schema = EventoHistoricoSchema()
eventos_historicos_schema = EventoHistoricoSchema(many=True)
