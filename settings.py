import uuid

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