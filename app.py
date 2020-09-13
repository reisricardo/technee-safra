from flask import Flask, Blueprint
from flask_cors import CORS
from models.jwt import configure_jwt
import os
from settings import *

#Habilita as cores no console log
os.system("")

#Import de blueprints da API
from api_v1 import blueprint as api_v1

app = Flask(__name__)

#Habilita o CORS
if CORS_ENABLE:
    CORS(app, supports_credentials=CORS_SUPPORT_CREDENTIALS)

#Configura o modulo JWT (Autenticacao)
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWT_ACCESS_TOKEN_EXPIRES
app.config['JWT_TOKEN_LOCATION'] = JWT_TOKEN_LOCATION
app.config['JWT_COOKIE_SECURE'] = JWT_COOKIE_SECURE
app.config['JWT_COOKIE_CSRF_PROTECT'] = JWT_COOKIE_CSRF_PROTECT
app.config['JWT_ALGORITHM'] = JWT_ALGORITHM
configure_jwt(app)

if __name__ == '__main__':
    try:
        #Registro dos blueprints
        app.register_blueprint(api_v1)

        #Remove o limite de cache do jinja, de 50 para -> infinito
        app.jinja_env.cache = {}
        app.run(host = FLASK_RUN_HOST, port = FLASK_RUN_PORT, debug = FLASK_DEBUG, threaded = FLASK_THREADED)
    except Exception as e:
        print(e)