from flask import Blueprint

eventoJson_bp = Blueprint('eventoJson', __name__)

from ..endpoint.eventoJson import *