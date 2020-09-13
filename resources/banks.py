############# Conjunto de rotas da coleção de bancos #############

from flask import request, jsonify
from flask_restx import Resource, Namespace
from flask_jwt_extended import (
    jwt_required, get_jwt_identity, create_access_token, create_refresh_token,
    set_access_cookies, set_refresh_cookies, unset_jwt_cookies, get_raw_jwt
)
from settings import *
from common.request_handler import request_handler
from common.utils import get_token, get_account_data
from models.db import database, driver as db_driver

import json
import datetime
import requests


banks_collection = Namespace('banks', description='Banks related operations.', ordered=True)

@banks_collection.route('/<string:bank>/clients/<string:identification>/synchronize')
class syncronize_accounts(Resource):
    def get(self, bank, identification):
        '''
        Responsável por procurar na coleção de APIs do open banking, as contas de um determinado usuário em uma determinada instituição
        '''
        url = request_handler(request)
        args = url.get_args()

        try:
           
            db_connection = database()
            conn, cursor = db_connection.open_connection()

            for institution in REGISTERED_INSTITUTIONS:
                token = get_token(institution)

                '''
                Nesse ponto eu vou utilizar duas premissas, devido a ausencia dessa rota na API disponibilizada.
                Premissa 1: A api disponibilizada pelos bancos contém uma rota que lista os usuários daquela instituição,
                e responde aproximadamente no seguinte formato:
                
                'Data' : [
                    {'AccountId' : '00711234511', 'Identification' : '12345678901211'},
                    {'AccountId' : '00711234522', 'Identification' : '12345678901222'},
                    {'AccountId' : '00711234533', 'Identification' : '12345678901233'}
                ]
                Abaixo sera possivel ver o mock dessa resposta pra cada instituição cadastrada
                '''
                if institution == 'SAFRA':
                    list_clients = {
                        'Data' : 
                            [
                                {'AccountId' : '00711234511', 'Identification' : '12345678901211'},
                                {'AccountId' : '00711234522', 'Identification' : '12345678901222'},
                                {'AccountId' : '00711234533', 'Identification' : '12345678901233'}
                            ]
                        
                    }
                if institution == 'PLAYER_I':
                    list_clients = {
                        'Data' : 
                            [
                                {'AccountId' : '0034145611', 'Identification' : '12345678901211'},
                                {'AccountId' : '0034145622', 'Identification' : '12345678901222'},
                                {'AccountId' : '0034145633', 'Identification' : '12345678901233'}
                            ]                    
                    }
                if institution == 'PLAYER_S':
                    list_clients = {
                        'Data' : 
                            [
                                {'AccountId' : '00335789311', 'Identification' : '12345678901211'},
                                {'AccountId' : '00335789322', 'Identification' : '12345678901222'},
                                {'AccountId' : '00335789333', 'Identification' : '12345678901233'}
                            ]                    
                    }

                for row in list_clients['Data']:
                    if(row['Identification'] == identification):
                    
                        data = get_account_data(institution, row['AccountId'], token)
                        
                        for transaction in data['data']['transaction']:
                            sql = '''
                                     
                                    INSERT INTO `open`.`aux_transactions` (`account_id`, `transaction_id`, `amount`, `currency`, `operation`, `booking_date`, `value_date`, `information`, `aux_banks_code`, `users_identification`) 
                                    VALUES(
                                        %(account_id)s, 
                                        %(transaction_id)s, 
                                        %(amount)s, 
                                        %(currency)s,
                                        %(operation)s,
                                        %(booking_date)s,
                                        %(value_date)s,
                                        %(information)s,
                                        %(aux_banks_code)s,
                                        %(users_identification)s                                        
                                    ) ON DUPLICATE KEY UPDATE amount = VALUES(amount), currency = VALUES(currency), operation = VALUES(operation), booking_date = VALUES(booking_date), value_date = VALUES(value_date), information = VALUES(information) 
                                '''                
                            val = {
                                'account_id': transaction['accountId'],
                                'transaction_id': transaction['transactionId'],
                                'amount': transaction['amount']['amount'],
                                'currency': transaction['amount']['currency'],
                                'operation': transaction['creditDebitIndicator'],
                                'booking_date': transaction['bookingDateTime'],
                                'value_date': transaction['valueDateTime'],
                                'information': transaction['transactionInformation'],
                                'aux_banks_code': transaction['proprietaryBankTransactionCode']['issuer'],
                                'users_identification': row['Identification']                                
                            }
                            cursor.execute(sql ,val)
                            conn.commit()
                            
                resp = jsonify({
                    'StatusId' : 'banks_synchronization_successful',
                    'StatusMessage' : 'Synchronization successful.',                    
                    'Links' : {
                        'Self' : url.self_url()                 
                    }
                })
                resp.status_code = 200            

        
        except db_driver.Error as e:
            
            resp = jsonify({
                'StatusId' : 'banks_database_error',
                'StatusMessage' : 'Database error.',
                'DescriptionError' : str(e),
                'Links' : {
                    'Self' : url.self_url()                 
                }
            })
            resp.status_code = 500
        except Exception as e:
            resp = jsonify({
                'StatusId' : 'banks_internal_error',
                'StatusMessage' : 'Synchronization error occurred.',
                'DescriptionError' : str(e),
                'Links' : {
                    'Self' : url.self_url()                 
                }
            })
            resp.status_code = 500
        finally:
            return resp    

        

@banks_collection.route('/<string:bank>/clients')
class list_clients(Resource):
    def get(self, bank):
        '''
        Rota responsável por 
        '''
        #Get de Authorization
        print(API_BANKS)
        for data_bank in API_BANKS:
            url_bank = API_BANKS[data_bank]['URL']
            url_token = API_BANKS[data_bank]['URL_TOKEN']
            api_key_authorization = API_BANKS[data_bank]['API_KEY']

            print(api_key_authorization, url_bank, url_token)

            
            
            '''
            Nesse ponto eu vou utilizar duas premissas, devido a ausencia dessa rota na API disponibilizada.
            Premissa 1: A api disponibilizada pelos bancos contém uma rota que lista os usuários daquela instituição,
            e responde aproximadamente no seguinte formato:
            
            'Data' : {
                {'AccountId' : '00711234511', 'Identification' : '12345678901211'},
                {'AccountId' : '00711234522', 'Identification' : '12345678901222'},
                {'AccountId' : '00711234533', 'Identification' : '12345678901233'}
            }
            
            Premissa 2: A nossa plataforma possui um "crawler" rodando 
            

            Nesse ponto, deveria existir um endpoint nas APIs de cada banco com a lista de clientes
            Eu vou considerar que esse dado chegou no seguinte formato arbitrário
            '''
            

            #Com essa informação, eu 

            print(auth_token)

            