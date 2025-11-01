import os, json

dados = {}

def load_dados():
    global dados
    try:
        with open('dados.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
    except FileNotFoundError:
        dados = {
            'clientes': [
                {'nome': 'JOÃO ALMEIDA DE SOUZA', 'idade': 21, 'cpf': '906.526.200-86'},
                {'nome': 'MARIA APARECIDA', 'idade': 37, 'cpf': '870.026.320-60'},
                {'nome': 'LUCA CARDOSO DA SILVA MELO', 'idade': 25, 'cpf': '490.665.810-50'},
                {'nome': 'DAVID PEREIRA LUSTOZA', 'idade': 49, 'cpf': '493.513.930-70'},
                {'nome': 'RODOLFO MOTA MONTEIRO', 'idade': 18, 'cpf': '360.314.650-60'},
                {'nome': 'ERI GOMES DE MORAIS', 'idade': 36, 'cpf': '648.125.840-51'},
                {'nome': 'PAULO MORAES DE JESUS NETO', 'idade': 39, 'cpf': '169.463.600-36'},
                {'nome': 'ITALO DUTRA SILVA', 'idade': 19, 'cpf': '727.997.820-78'},
                {'nome': 'VICTOR GUIMARÃES SILVA', 'idade': 52, 'cpf': '365.311.790-90'}
            ],
            'produtos': [
                {'codigo': 1, 'nome': 'arroz', 'preco': 5.50, 'custo': 4.00, 'lucro': 1.50, 'estoque': 50, 'vendaPorDia': 10},
                {'codigo': 2, 'nome': 'feijão', 'preco': 7.00, 'custo': 5.50, 'lucro': 1.50, 'estoque': 30, 'vendaPorDia': 15},
                {'codigo': 3, 'nome': 'macarrão', 'preco': 3.20, 'custo': 2.50, 'lucro': 0.70, 'estoque': 80, 'vendaPorDia': 13},
                {'codigo': 4, 'nome': 'leite', 'preco': 4.50, 'custo': 3.80, 'lucro': 0.70, 'estoque': 20, 'vendaPorDia': 8},
                {'codigo': 5, 'nome': 'pão', 'preco': 2.00, 'custo': 1.50, 'lucro': 0.50, 'estoque': 100, 'vendaPorDia': 19}
            ],
            'vendas': []
        }

def save_dados():
    with open('dados.json', 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
