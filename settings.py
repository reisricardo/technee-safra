import uuid
import base64 

############# Configurações da aplicação #############
FLASK_DEBUG = True
FLASK_RUN_HOST = '127.0.0.1'
FLASK_RUN_PORT = 8000
FLASK_THREADED = True

############# Configurações do CORS #############
CORS_ENABLE = True
CORS_SUPPORT_CREDENTIALS = True

############# Configurações do Token JWT #############
JWT_SECRET_KEY = uuid.uuid4().hex
JWT_ACCESS_TOKEN_EXPIRES = 7200
JWT_TOKEN_LOCATION = ['cookies']
JWT_COOKIE_SECURE = False
JWT_COOKIE_CSRF_PROTECT = True
JWT_ALGORITHM = 'HS256'

############# Configurações da Database #############
DATABASE_USER = 'open-user'
DATABASE_PASS = '1UlCjKJT'
DATABASE_HOST = '127.0.0.1'
DATABASE_PORT = '3306'

############# Configurações de URLs #############
SITE_URL = 'http://127.0.0.1/safra-open'
LOGIN_URL = '/login.html'
LOGIN_REDIRECT_URL  = '/home.html' 

API_URL = 'http://127.0.0.1:8000/open-banking/v1/'

############# Configurações de APIs Bancárias #############
API_BANKS = {
    'SAFRA' : {
        'URL' : 'https://af3tqle6wgdocsdirzlfrq7w5m.apigateway.sa-saopaulo-1.oci.customer-oci.com/fiap-sandbox',
        'CLIENT_ID' : 'f9d3cd9600874ac2803d03ca709b78eb',
        'SECRET_ID' : '1a2075e3-b15e-4324-902c-0f12f8f08082',
        'API_KEY' : base64.b64encode(bytes('f9d3cd9600874ac2803d03ca709b78eb' + ':' + '1a2075e3-b15e-4324-902c-0f12f8f08082', 'utf-8')),
        'URL_TOKEN' : 'https://idcs-902a944ff6854c5fbe94750e48d66be5.identity.oraclecloud.com/oauth2/v1/token',
        
        'URL_EXTRACT' : '/open-banking/v1/accounts/{}/transactions'
    },
    'PLAYER_I' : {
        'URL' : 'https://run.mocky.io/v3',
        'CLIENT_ID' : 'f9d3cd9600874ac2803d03ca709b78eb',
        'SECRET_ID' : '1a2075e3-b15e-4324-902c-0f12f8f08082',
        'API_KEY' : base64.b64encode(bytes('f9d3cd9600874ac2803d03ca709b78eb' + ':' + '1a2075e3-b15e-4324-902c-0f12f8f08082', 'utf-8')),
        'URL_TOKEN' : 'https://run.mocky.io/v3/f75d63b2-9adc-4dbb-b88a-ff2c699e0c91',
        'URL_EXTRACT' : '/11c86aad-5b3b-4bdb-bb0a-e945b90c4c29'
    },
    'PLAYER_S' : {
        'URL' : 'https://run.mocky.io/v3',
        'CLIENT_ID' : 'f9d3cd9600874ac2803d03ca709b78eb',
        'SECRET_ID' : '1a2075e3-b15e-4324-902c-0f12f8f08082',
        'API_KEY' : base64.b64encode(bytes('f9d3cd9600874ac2803d03ca709b78eb' + ':' + '1a2075e3-b15e-4324-902c-0f12f8f08082', 'utf-8')),
        'URL_TOKEN' : 'https://run.mocky.io/v3/f75d63b2-9adc-4dbb-b88a-ff2c699e0c91',
        'URL_EXTRACT' : '/dca0e8e5-a5a0-4dbe-aa80-9b561759c3a6'
    }
}

REGISTERED_INSTITUTIONS = ['SAFRA', 'PLAYER_I', 'PLAYER_S']
