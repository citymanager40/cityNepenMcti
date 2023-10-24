from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.subcategoriaModel import Subcategoria

class subcategoriaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Subcategoria
        exclude = ('dataFim',)

subcategoria_schema = subcategoriaSchema()
subcategorias_schema = subcategoriaSchema(many=True)