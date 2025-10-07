import produto as pd

# def atualizar_funcionarios(func):
#     funcionarios_ordenados = sorted(func, key=lambda x: x['nome'].lower())
#     print(funcionarios_ordenados)

def listar_funcionarios(funcionarios):
    funcionarios_ordenados = sorted(funcionarios, key=lambda x: x['nome'])
    print('_=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+_')
    print('|     QUADRO DE FUNCIONÁRIOS ATUALIZADO      |')
    print('*--------------------------------------------*')
    print('\n ____________________________________________ ')
    for i in funcionarios_ordenados:
        print(f"|Nome: {i['nome']:<19} | Idade: {i['idade']:<3} anos.|")
        print('*--------------------------------------------*')

    input('\nPressione qualquer tecla.')

funcionarios = [
    {'nome': 'JULIANA EVANGELISTA', 'idade': 21, 'senha': '1234'},
    {'nome': 'RAFAEL PIRÔPO', 'idade': 30, 'senha': '1414'},
    {'nome': 'KAIQUE AQUINO', 'idade': 20, 'senha': '1515'},
    {'nome': 'HUDSON COIMBRA', 'idade': 18, 'senha': '1616'},
    {'nome': '0', 'idade': 0, 'senha': '0'}
]


