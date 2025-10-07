import produto as pd, math, os

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

# --- 1. RELATÓRIO DE PRODUTOS MAIS VENDIDOS ---

# Usamos a função sorted() para criar uma NOVA lista ordenada.
# O 'key' diz ao Python para ordenar com base no valor de 'vendaPorDia'.
# 'reverse=True' ordena do maior para o menor.

def maisVendidos(produtosComLucro):
    os.system('cls')
    mais_vendidos = sorted(produtosComLucro, key=lambda p: p['vendaPorDia'], reverse=True)

    print("PRODUTOS MAIS VENDIDOS")
    print("Ranking por média de vendas diárias:\n")
    for i, produto in enumerate(mais_vendidos, start=1):
        # O f-string formata a saída de forma legível
        print(f"{i}º lugar: {produto['nome'].title()} ({produto['vendaPorDia']} vendas/dia)")
    input('\nPressione qualquer tecla para continuar.')


# --- 2. RELATÓRIO DE PREVISÃO DE FALTA DE ESTOQUE ---

# Aqui, a chave de ordenação é o resultado da divisão do estoque pela venda diária.
# Isso nos dá o número de dias restantes para o estoque acabar.
# Não usamos 'reverse=True' porque queremos ver os que acabarão PRIMEIRO.
# Adicionamos uma verificação para evitar divisão por zero se um produto não vender.
def previsaoFalta(produtosComLucro):
    os.system('cls')
    previsao_falta = sorted(produtosComLucro, key=lambda p: p['estoque'] / p['vendaPorDia'] if p['vendaPorDia'] > 0 else float('inf')
    )

    print("\nPREVISÃO DE FALTA DE ESTOQUE")
    print("Produtos com maior risco de esgotamento:\n")
    for produto in previsao_falta:
        if produto['vendaPorDia'] > 0:

            # math.floor() arredonda o número de dias para baixo
            dias_restantes = math.floor(produto['estoque'] / produto['vendaPorDia'])
            print(f"○ {produto['nome']}: Estoque para aproximadamente {dias_restantes} dias ({produto['estoque']} un. / {produto['vendaPorDia']} un. por dia)")
        else:
            print(f"○ {produto['nome']}: Sem vendas diárias, não há previsão de falta.")
    input('\nPressione qualquer tecla para continuar.')




