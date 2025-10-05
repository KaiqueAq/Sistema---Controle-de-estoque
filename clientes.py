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
    print("Cadastrarmento de Cliente")
    nome = input("Digite o nome do cliente: ").upper() #receber letras minúsculas
    idade = int(input("Digite a idade do {nome}: "))
    cpf = input(f"Digite o CPF do {nome}: ")

    novocliente = {
        'nome': nome, 'idade': idade, 'cpf': cpf
    }
    clientes.append(novocliente)

    print(f"Cliente{nome}cadastramento realizado!")
    
def nome(cliente): 
    clientes.sort(key=nome)
    for i in clientes:
        print(f"{i['nome']} - {i['idade']} anos - CPF: {i['cpf']}")
    return cliente['nome']

def comprarProduto():
    pass
    