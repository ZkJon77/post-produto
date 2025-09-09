from models.carro_models import Carro
from db import db
import json
from flask import make_response

from models.carro_models import Carro  # Importa o modelo Carro
from db import db  # Importa a conexão com o banco de dados
import json
from flask import make_response
# Função para obter todos os carros
def get_carros():
    carros = Carro.query.all()  # Busca todos os carros no banco de dados
    response = make_response(
        json.dumps({
            'mensagem': 'Lista de carros.',
            'dados': [carro.json() for carro in carros]  # Converte os objetos de carro para JSON
        }, ensure_ascii=False, sort_keys=False)  # Mantém caracteres especiais corretamente formatados
    )
    response.headers['Content-Type'] = 'application/json'  # Define o tipo de conteúdo como JSON
    return response
def create_carro(carro_data):
    novo_carro = Carro(
        modelo=carro_data['modelo'],
        marca=carro_data['marca'],
        ano=carro_data['ano']
    )

    db.session.add(novo_carro)
    db.session.commit()
    response = make_response(
        json.dumps({
            'mensagem': 'Carro cadastrado com sucesso.',
            'carro': novo_carro.json()
        }, sort_keys=False)
    )

    response.headers['Content-Type'] = 'application/json'
    return response
