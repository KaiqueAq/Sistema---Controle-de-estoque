#Cadastramento
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

def cadastrar_cliente():
    print("Cadastro de Cliente")
    nome =input("Digite o nome do cliente: "). upper()
    while True:
        try:
            idade = int(input(f"Digite a idade de {nome}: "))
            break
        except ValueError:
            print("Idade inválida")
    cpf = input(f"Digite o cpf {nome}: ")
    clientes.append({'nome': nome, 'idade': idade, 'cpf': cpf})
    print(f"Cliente {nome} cadastramento com sucesso!")

def cadastro_nomes(cliente):
    return cliente['nome']

def listar_clientes(cliente):
    print("Lista de clientes do Mercado atualizada")
    clientes.sort(key=cadastro_nomes)
    for i in clientes:
        print(f"{i['nome']} - {i['idade']} aos - CPF {i['cpf']} ")

while True:
    print ("1. Cadastrar Novo Cliente")
    print ("2. Listar Clientes")
    print( "3. Sair")
    opcao = input("Escolha uma opção")
    if opcao == '1':
        cadastrar_cliente()
    elif opcao == '2':
        listar_clientes()
    elif opcao == '3':
        print("Sair")
        break
    else:
        print("inválida")


def comprarProduto():
    pass
    