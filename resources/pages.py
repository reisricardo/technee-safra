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
        Carrega a pagina home
        '''

        resp = make_response(render_template('home.html', 
        api_url = API_URL
        ))
        resp.headers['Content-Type'] = "text/html"

        return resp

@pages_collection.route('/login')
class render_login(Resource):
    def get(self):
        '''
        Carrega a pagina login
        '''

        resp = make_response(render_template('login.html', 
        api_url = API_URL
        ))
        resp.headers['Content-Type'] = "text/html"

        return resp

@pages_collection.route('/contract')
class render_login(Resource):
    def get(self):
        '''
        Carrega a pagina contract
        '''

        resp = make_response(render_template('contract.html', 
        api_url = API_URL
        ))
        resp.headers['Content-Type'] = "text/html"

        return resp

@pages_collection.route('/investment')
class render_login(Resource):
    def get(self):
        '''
        Carrega a pagina investiment
        '''

        resp = make_response(render_template('investment.html', 
        api_url = API_URL
        ))
        resp.headers['Content-Type'] = "text/html"

        return resp
    
@pages_collection.route('/play')
class render_login(Resource):
    def get(self):
        '''
        Carrega a pagina investiment
        '''

        resp = make_response(render_template('play.html', 
        api_url = API_URL
        ))
        resp.headers['Content-Type'] = "text/html"

        return resp