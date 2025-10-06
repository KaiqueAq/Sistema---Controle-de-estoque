import produto as pd

def atualizar_gerente(func):
    gerente_ordenados = sorted(func, key=lambda x: x['nome'].lower())
    input(gerente_ordenados)

gerente = [
    {'nome': 'JULIANA EVANGELISTA', 'senha': '1234'},
    {'nome': 'RAFAEL PIRÔPO', 'senha': '1414'},
    {'nome': 'KAIQUE AQUINO', 'senha': '1515'},
    {'nome': 'HUDSON COIMBRA', 'senha': '1616'},
    {'nome': '0', 'senha': '0'}
]