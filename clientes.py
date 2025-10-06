#Cadastramento
import produto as pd
import funcionarios as fc

clientes = [
    {'nome': 'JOÃO ALMEIDA DE SOUZA', 'idade': 21, 'cpf': '906.526.200-86'},
    {'nome': 'MARIA APARECIDA', 'idade': 37, 'cpf': '870.026.320-60'},
    {'nome': 'LUCA CARDOSO DA SILVA MELO', 'idade': 25, 'cpf': '490.665.810-50'},
    {'nome': 'DAVID PEREIRA LUSTOZA', 'idade': 49, 'cpf': '493.513.930-70'},
    {'nome': 'RODOLFO MOTA MONTEIRO', 'idade': 18, 'cpf': '360.314.650-60'},
    {'nome': 'ERI GOMES DE MORAIS', 'idade': 36, 'cpf': '648.125.840-51'},
    {'nome': 'PAULO MORAES DE JESUS NETO', 'idade': 39, 'cpf': '169.463.600-36'},
    {'nome': 'ITALO DUTRA SILVA', 'idade': 19, 'cpf': '727.997.820-78'},
    {'nome': 'VICTOR GUIMARÃES SILVA', 'idade': 52, 'cpf': '365.311.790-90'}
]

# def ordem(x):
#     return x['nome']
# clientesOrdenados = sorted(clientes, key=ordem)
# for c in clientesOrdenados:
#     print(c)

# for c in clientesOrdenados2:
#     print('|            nome            | idade |      CPF      |')
#     print(f'|{c['nome']:^28}|{c['idade']:^7}|{c['cpf']:^15}|')
#     print('=+'*27)

def cadastrar_cliente():
    print("Cadastro de Cliente")
    nome =input("Digite o nome do cliente: "). upper()
    while True:
        try:
            idade = int(input(f"Digite a idade de {nome}: "))
            if idade < 18:
                print("Menor de 18 anos não pode ser cadastrado.")
                continue
            break
        except ValueError:
            print("Por favor, digite uma idade inválida")
            continue
    cpf = input(f"Digite o cpf {nome}: ")
    clientes.append({'nome': nome, 'idade': idade, 'cpf': cpf})
    print(f"Cliente {nome} cadastramento com sucesso!")

def cadastro_nomes(cliente):
    return cliente['nome']

def listar_clientes(clientes):
    print("Lista de clientes do Mercado atualizada")
    clientes.sort(key=clientes['nome'])
    for i in clientes:
        print(f"{i['nome']} - {i['idade']} aos - CPF {i['cpf']} ")

def remover_cliente():
    nome_remover = input("Digite o nome do cliente a ser removido: "). upper()
    for cliente in clientes:
        if cliente['nome'] == nome_remover:
            clientes.remove(cliente)
            print(f"\n Cliente {nome_remover} removido com sucesso!")
            return
    print(f"\n Cliente {nome_remover} não encontrado.")
import os

#while True:
#    print("\n1. Cadastrar Novo Cliente")
#    print("2. Listar Clientes")
#    print("3. Remover Cliente")
#    print("4. Sair")
#    opcao = input("Escolha uma opção: ")
#    if opcao == '1':
#        cadastrar_cliente()
#    elif opcao == '2':
#        listar_clientes()
#    elif opcao == '3':
#        remover_cliente()
#    elif opcao == '4':
#        print("Saindo do sistema...")
#        break
#    else:
#        print("Opção inválida. Digite 1, 2, 3 ou 4.")

def comprarProduto():
    produtos_ordenados = sorted(pd.produtos, key=lambda x: x['nome'])
    print("\nProdutos:")
    for p in produtos_ordenados:
        print(f"{p['nome']} - Preço: {p['preco']} - Custo: {p['custo']} - Estoque: {p['estoque']} - Vendas por dia: {p['vendaPorDia']}")
 
    while True:
        qualProduto = input('\nQual produto deseja comprar? ')

        for i in pd.produtos:
            if i['nome'] == qualProduto:
                qualQntd = int(input('Informe a quantidade desejada: '))
                if qualQntd > i['estoque']:
                    input('Estoque não supre o pedido.')
                elif qualQntd <= i['estoque']:
                    i['estoque'] -= qualQntd



                    input(f'Compra realizada com sucesso. Restam {i['estoque']} unidades.')
                    if i['estoque'] <= 0:
                        pd.produtos.remove(i)
                        input('Estoque zerado. Produto removido.')
                        return
                    return
                    
        if i['nome'] != qualProduto:
            input('Inválido. Tente novamente.')
            continue

