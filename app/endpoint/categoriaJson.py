from flask_login import login_required
from flask import jsonify, request
from sqlalchemy import and_
from app.models.categoriaModel import Categoria
from app.models.subcategoriaModel import Subcategoria
from ..rotas.categoriaJsonRout import categoriaJson_bp
from ..serializable.categoriaSchema import categoria_schema
from ..serializable.subcategoriaSchema import subcategoria_schema

class categoriaJson():

    @categoriaJson_bp.route('/categorias', methods=["GET"])
    # @login_required
    def categorias():

        try:
            listCategoria = Categoria.query.filter(Categoria.dataFim.is_(None)).all()

            if listCategoria is None:
                return jsonify({"Status": "Nenhuma Ocorrência Encontrada"}), 200
            
            categoria = categoria_schema.dump(listCategoria)

            return jsonify({"categorias": categoria})
        
        except Exception as e:
            return jsonify({"Status:" : str(e)}), 400
        
    @categoriaJson_bp.route('/subcategoria', methods=["POST"])
    # @login_required
    def subcategoria():

        data = request.get_json()

        if 'idCategoria' not in data:
            return jsonify({"Status": "Campo 'idCategoria' ausente no JSON"}), 400

        idCategoria = data['idCategoria']

        try:
            subcategoria = Subcategoria.query.filter(and_(Subcategoria.dataFim.is_(None), Subcategoria.idCategoria == idCategoria)).first()

            if subcategoria is None:
                return jsonify({"Status": "Nenhuma Ocorrência Encontrada"}), 200
            
            return subcategoria_schema.dump(subcategoria)
        
        except Exception as e:
            return jsonify({"Status:" : str(e)}), 400        


