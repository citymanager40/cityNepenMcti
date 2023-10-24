from flask import Blueprint

categoriaJson_bp = Blueprint('categoriaJson', __name__)

from ..endpoint.categoriaJson import *