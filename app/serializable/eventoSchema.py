from marshmallow import Schema, fields, pre_dump
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.eventoModel import Evento
import base64

class EventoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Evento

    file = fields.Method("encode_large_binary")

    def encode_large_binary(self, obj):
        if obj.file:
            return base64.b64encode(obj.file).decode('utf-8')
        return None