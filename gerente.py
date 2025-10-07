import produto as pd

#def atualizar_gerente(func):
#    gerente_ordenados = sorted(func, key=lambda x: x['nome'].lower())
#    input(gerente_ordenados)

gerenteConta = [
     {'nome': '1', 'senha': '1'}
     ]

funcionarios = [
    {'nome': 'JULIANA EVANGELISTA', 'senha': '1234'},
    {'nome': 'RAFAEL PIRÔPO', 'senha': '1414'},
    {'nome': 'KAIQUE AQUINO', 'senha': '1515'},
    {'nome': 'HUDSON COIMBRA', 'senha': '1616'},
    {'nome': '0', 'senha': '0'}
]



def atualizar_funcionarios(funcionarios):
    while True:
        print("lista de funcionarios:")
        for i, f in enumerate(funcionarios):
            print(f"{i + 1}. {f['nome']}")
            demitir = input("Digite o nome do funcionário a ser demitido (ou 'sair' para cancelar): ").upper()
            if demitir == 'SAIR':
                 print("Encerrando atualizações de funcionários.")


        for f in funcionarios:
                if f['nome'] == demitir:
                    funcionarios.remove(f)
                print(f"{demitir} foi removido da lista.")
        else:
            print("Funcionário não encontrado.")
            funcionarios = sorted(funcionarios, key=lambda x: x['nome'].lower())
            return funcionarios
        