import produto as pd

def atualizar_funcionarios(func):
    funcionarios_ordenados = sorted(func, key=lambda x: x['nome'].lower())
    input(funcionarios_ordenados)

funcionarios = [
    {'nome': 'JULIANA EVANGELISTA', 'senha': '1234'},
    {'nome': 'RAFAEL PIRÔPO', 'senha': '1414'},
    {'nome': 'KAIQUE AQUINO', 'senha': '1515'},
    {'nome': 'HUDSON COIMBRA', 'senha': '1616'},
    {'nome': '0', 'senha': '0'}
]


