from flask import Blueprint
from flask_restx import Api

from resources.pages import pages_collection
from resources.users import users_collection
from resources.banks import banks_collection

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

api.add_namespace(pages_collection)
api.add_namespace(users_collection)
api.add_namespace(banks_collection)