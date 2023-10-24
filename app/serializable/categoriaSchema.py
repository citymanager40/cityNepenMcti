from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.categoriaModel import Categoria

class categoriaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Categoria
        exclude = ('dataFim',)

categoria_schema = categoriaSchema(many=True)        