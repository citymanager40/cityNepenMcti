from flask import Blueprint

registerJson_bp = Blueprint('registerJson', __name__)

from ..endpoint.registerJson import *