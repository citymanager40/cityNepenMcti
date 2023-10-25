from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..models.statusEventoModel import StatusEvento

class statusSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = StatusEvento
        exclude = ('dataFim',)

status_schema = statusSchema(many=True)        