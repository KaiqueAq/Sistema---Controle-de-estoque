import os, funcionarios as fc

#def atualizar_gerente(func):
#    gerente_ordenados = sorted(func, key=lambda x: x['nome'].lower())
#    input(gerente_ordenados)

gerenteConta = [
     {'nome': 'WHASHINGTON', 'senha': '1'},
     {'nome': '1', 'senha': '1'}
]

def contasDisponiveis():
    os.system('cls')
    print('_=+=+=+=+=+=+=+=+=+=+=+=_')
    print('| HACKER PROMPT DISPLAY |')
    print('*-----------------------*')
    print('Contas disponíveis (Gerência): ')
    print(' ________________________________')
    print('|       Usuário       | Password |')
    print('*--------------------------------*')
    for c in gerenteConta:
        print(f'|{c['nome']:<21}|{c['senha']:^10}|')
    print('*--------------------------------*')

    print('\nContas disponíveis (Funcionários): ')
    print(' ________________________________')
    print('|       Usuário       | Password |')
    print('*--------------------------------*')
    for f in fc.funcionarios:
        print(f'|{f['nome']:<21}|{f['senha']:^10}|')
    print('*--------------------------------*')

def atualizar_funcionarios(funcionario):
    while True:
        os.system('cls')

        fc.listar_funcionarios_att(funcionario)

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
        