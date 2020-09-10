############# Conjunto de rotas da coleção de usuários #############

from flask import request, jsonify
from flask_restx import Resource, Namespace
from flask_jwt_extended import (
    jwt_required, get_jwt_identity, create_access_token, create_refresh_token,
    set_access_cookies, set_refresh_cookies, unset_jwt_cookies, get_raw_jwt
)
from settings import *
from common.request_handler import request_handler
from models.user import user
from models.db import database, driver as db_driver

import datetime

from Crypto.Hash import SHA256

users_collection = Namespace('users', description='Users related operations.')

@users_collection.route('/<int:identification>/authenticate')
class user_authenticate(Resource):
    def post(self, identification):
        '''
        Performs user authentication and returns access tokens (2h)
        '''
        url = request_handler(request)
        args = url.get_args()

        try:
           
            db_connection = database()
            conn, cursor = db_connection.open_connection()
            
            #Checa se existe informação no body
            if 'payload' in args:
                current_user = user() 
                current_user.uid = args['payload']          
                current_user.identification = identification
                registered_user, current_user = current_user.check_user_register(conn, cursor)

                #Caso o usuário seja válido, retorna as informações
                if registered_user:
                    access_token = create_access_token(identity=identification)
                    refresh_token = create_refresh_token(identity=identification)
                    
                    payload = {
                        "Identification" : current_user.identification,
                        "Name" : current_user.name,                
                        "CreationDate" : current_user.creation_date,    
                        "FailedAttempts" : current_user.failed_attempts,
                        "BlockedAccount" : current_user.blocked_account                        
                    }

                    resp = jsonify({
                        'Data': {
                            'User' : payload,
                            'Access' : {
                                'AccessToken' : access_token,
                                'RefreshToken' : refresh_token                                                            
                            }
                        },
                        'StatusID' : 'users_successful_authentication',
                        'StatusMessage' : 'Successful authentication.',
                        'Links' : {
                            'Self' : url.self_url(),
                            'Next' : SITE_URL + LOGIN_REDIRECT_URL               
                        }
                    })
                    resp.status_code = 200
                    set_access_cookies(resp, access_token)
                
                else:
                    resp = jsonify({                        
                        'StatusID' : 'users_invalid_credentials',
                        'StatusMessage' : 'Invalid credentials.',
                        'Links' : {
                            'Self' : url.self_url()                
                        }
                    })
                    resp.status_code = 401
            else: 

                resp = jsonify({                        
                    'StatusID' : 'users_missing_fields',
                    'StatusMessage' : 'There are missing fields in your request.',
                    'Links' : {
                        'Self' : url.self_url()                
                    }
                })
                resp.status_code = 401
            
        except db_driver.Error as e:
            
            resp = jsonify({
                'StatusId' : 'users_database_error',
                'StatusMessage' : 'Database error.',
                'DescriptionError' : str(e),
                'Links' : {
                    'Self' : url.self_url()                 
                }
            })
            resp.status_code = 500
        except Exception as e:
            resp = jsonify({
                'StatusId' : 'users_internal_error',
                'StatusMessage' : 'Authentication error occurred.',
                'DescriptionError' : str(e),
                'Links' : {
                    'Self' : url.self_url()                 
                }
            })
            resp.status_code = 500
        finally:
            return resp
        