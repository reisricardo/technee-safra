from flask import request, current_app

class request_handler:
    '''
    Biblioteca com métodos para manipulação das requisições
    '''

    def __init__(self, request_obj):
        self.request = request_obj

    def get_version(self):
        '''
        Retorna a versão da API
        '''
        url = request.path
        url = url.split("/")
        return url[2]
    
    def get_args(self):
        '''
        Retorna os argumentos enviados com a requisição
        Método POST => Retorna argumentos do body
        Método GET => Retorna argumentos da query string
        Método PUT => Retorna argumentos do body
        '''

        if request.method == 'POST':
            return request.form
        elif request.method == 'GET':
            return request.args
        elif request.method == 'PUT':
            return request.form

    def self_url(self):
        '''
        Retornaa url de requisição
        '''
        return request.url