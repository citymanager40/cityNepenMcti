from flask_login import login_required
from flask import jsonify
from app.models.categoriaModel import Categoria
from ..rotas.eventoJsonRout import eventoJson_bp

class eventoJson():

    @eventoJson_bp.route('/eventoJson', methods=['GET'])
    # @login_required
    def iniciar_json():
        listCategoria = Categoria.query.filter(Categoria.dataFim.is_(None)).all()
        categorias_json = [{"id": cat.id, "txtCategoria": cat.txtCategoria} for cat in listCategoria]
        return jsonify({"listCategoria": categorias_json})
