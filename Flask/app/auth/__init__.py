from flask import Blueprint

# todas las rutas que comiencen con /auth van a ser rediregidas a este Blueprint
auth = Blueprint('auth', __name__, url_prefix='/auth')

from . import views