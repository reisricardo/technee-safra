from flask import Blueprint
from flask_restx import Api



blueprint = Blueprint('api_v1', __name__, url_prefix='/open-banking/v1')
api = Api(
    blueprint, 
    title='Safra Open API', 
    version='1.0.0', 
    description='Safra Open feature set',
    contact='',
    catch_all_404s = True,
    ordered = True
)