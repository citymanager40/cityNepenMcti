from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.statusEventoModel import StatusEvento

class StatusEventoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = StatusEvento