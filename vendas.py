import math, os

vendas = []
carrinhoDeCompra = []
totalDeVenda = 0 
lucroDaVenda = 0

# vendas = [
#    {
#        'cliente_cpf': '906.526.200-86',
#        'pd.produtosComLucro': [
#            {'nome': 'Arroz', 'quantidade': 2},
#            {'nome': 'Feijão', 'quantidade': 1}
#        ],
#        'total': 18.00,
#        'lucro': 3.50,
#        'data': '2023-10-01'
#      }
# ]

# Usamos a função sorted() para criar uma NOVA lista ordenada.
# O 'key' diz ao Python para ordenar com base no valor de 'vendaPorDia'.
# 'reverse=True' ordena do maior para o menor.

def maisVendidos(produtosComLucro):
    os.system('cls')
    mais_vendidos = sorted(produtosComLucro, key=lambda p: p['vendaPorDia'], reverse=True)

    print("_+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=_")
    print("|       PRODUTOS MAIS VENDIDOS       |")
    print("*+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=*")
    print("\nRanking por média de vendas diárias:")
    print(' _________________________________________')
    print('| Colocação |     Produto     | Venda/dia |')
    for i, produto in enumerate(mais_vendidos, start=1):
        print(f"|   {i:>3}º    | {produto['nome']:<16}|{produto['vendaPorDia']:^11}|")
    print('*=========================================*')
    input('\nPressione qualquer tecla para continuar.')


# Aqui, a chave de ordenação é o resultado da divisão do estoque pela venda diária.
# Isso nos dá o número de dias restantes para o estoque acabar.
# Não usamos 'reverse=True' porque queremos ver os que acabarão PRIMEIRO.
# Adicionamos uma verificação para evitar divisão por zero se um produto não vender.
def previsaoFalta(pds):
    os.system('cls')
    previsao_falta = sorted(pds, key=lambda p: p['estoque'] / p['vendaPorDia'] if p['vendaPorDia'] > 0 else float('inf')
    )

    print("_+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=_")
    print("|     PREVISÃO DE FALTA DE ESTOQUE     |")
    print("*+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=*")
    print("\nProdutos com maior risco de esgotamento:")
    print(' _______________________________________________________________')
    print('|     Produto     | Estoque aproximado | Em estoque | Venda/dia |')
    for produto in previsao_falta:
        if produto['vendaPorDia'] > 0:

            # Aqui tava dando número quebrado as vezes, aí usamos a biblioteca de matemática pra arredondar o número de dias para baixo
            dias_restantes = math.floor(produto['estoque'] / produto['vendaPorDia'])
            print(f"|{produto['nome']:<17}|     {dias_restantes:>3} dias       | {produto['estoque']:>5} un.  |{produto['vendaPorDia']:5} un.  |")
        else:
            print('*---------------------------------------------------------------*')
            print(f"|{produto['nome']:<17}|Sem vendas diárias, não há previsão de falta.|")
    print('*---------------------------------------------------------------*')
    input('\nPressione qualquer tecla para continuar.')

