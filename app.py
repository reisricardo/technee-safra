from flask import Flask, Blueprint
from flask_cors import CORS
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

if __name__ == '__main__':
    try:
        #Registro dos blueprints
        app.register_blueprint(api_v1)

        #Remove o limite de cache do jinja, de 50 para -> infinito
        app.jinja_env.cache = {}
        app.run(   
            host = FLASK_RUN_HOST,
            port = FLASK_RUN_PORT,
            debug = FLASK_DEBUG,
            threaded = FLASK_THREADED
        )
    except Exception as e:
        print(e)