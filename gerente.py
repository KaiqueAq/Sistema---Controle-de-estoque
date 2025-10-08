import os, funcionarios as ff

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

def atualizar_funcionarios(funcionario):
    while True:
        os.system('cls')

        ff.listar_funcionarios_att(funcionario)

        opcao = input(f'Você deseja demitir algum funcionário? (s/n) ').lower()

        if opcao == 's':
            demitir = input("Digite o nome do funcionário a ser demitido (ou sair): ").upper().strip()
            if demitir == 'SAIR':
                return
            for func in funcionario:
                if func['nome'] == demitir:
                    funcionario.remove(func)
                    input('Funcionário demitido.')
                    print(funcionario)
                    os.system('cls')
                    return
            if demitir not in func['nome']:
                input('Funcionário não encontrado.')
                os.system('cls')
                break
        elif opcao == 'n':
            break
        else:
            input('Opção inválida. Tente novamente.')
            continue


        # for f in funcionarios:
        #         if f['nome'] == demitir:
        #             funcionarios.remove(f)
        #         print(f"{demitir} foi removido da lista.")
        # else:
        #     print("Funcionário não encontrado.")
        #     funcionarios = sorted(funcionarios, key=lambda x: x['nome'].lower())
        #     return funcionarios
        