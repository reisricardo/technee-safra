<p align="center">
<img src="https://raw.githubusercontent.com/reisricardo/static/master/logo-safra-open.svg">
</p>

**Safra Open a mais completa plataforma Open Banking.**

## Descrição
A plataforma Safra Open foi desenvolvida durante o Hackathon Technee do Banco Safra.
Foi implementada como um serviço em **Python + Flask** utilizando a biblioteca **Flask-RESTX**. Utiliza o mecanismo de template **Jinja** para prover todo o Front-end.

<p align="center">
  <img width=250 src="https://raw.githubusercontent.com/reisricardo/static/master/arq2.png">
</p>

## Pré-Requisitos
- Python 3.6+
- Banco de Dados MySQL 8.0 (Schema no repositório)

## Organização
![](https://raw.githubusercontent.com/reisricardo/static/master/org.png)

## Configuração
O arquivo **settings.py**, contém todas as configurações para o correto funcionamento da aplicação

Os dados de conexão com o MySQL devem ser editados de acordo com a instância da máquina.


    ############# Configurações da Database #############
    DATABASE_USER = 'user'
    DATABASE_PASS = 'password'
    DATABASE_HOST = '127.0.0.1'
    DATABASE_PORT = '3306'

## Rodando

- Instalando a biblioteca [virtual env](https://pypi.org/project/virtualenv/ "virtual env")

```bash
pip install virtualenv
```

- Criando uma virtual env 

```bash
virtualenv venv
```
- Ativando a virtual env

```bash
source venv/Scripts/Activate
```

- Instalando os requirements.txt

```bash
pip install -r requirements.txt
```

- Rodando a aplicação

```bash
python app.py
```


![](https://raw.githubusercontent.com/reisricardo/static/master/run.png)


- Visualizando a documentação da API
```bash
http://127.0.0.1:8000/open-banking/v1
```
![](https://raw.githubusercontent.com/reisricardo/static/master/api.png)


## Time 9
