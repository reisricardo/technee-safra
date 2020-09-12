from flask import render_template, make_response
from flask_restx import Resource, Namespace
from flask_jwt_extended import (
    jwt_required, get_raw_jwt, get_jwt_identity
)

from settings import *

pages_collection = Namespace('pages', description='Render pages operations.')


@pages_collection.route('/home')
class render_home(Resource):
    def get(self):
        '''
        Loads the homepage
        '''

        resp = make_response(render_template('home.html', 
        api_url = API_URL
        ))
        resp.headers['Content-Type'] = "text/html"

        return resp
