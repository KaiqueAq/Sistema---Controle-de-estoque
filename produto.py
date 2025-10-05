# Produtos
#Estoque
produtos = [
    {'nome': 'arroz', 'preco': 5.50, 'custo': 4.00, 'estoque': 50, 'vendaPorDia': 10},
    {'nome': 'feijão', 'preco': 7.00, 'custo': 5.50, 'estoque': 30,'vendaPorDia': 15},
    {'nome': 'macarrão', 'preco': 3.20, 'custo': 2.50, 'estoque': 80,'vendaPorDia': 13},
    {'nome': 'leite', 'preco': 4.50, 'custo': 3.80, 'estoque': 20,'vendaPorDia': 8},
    {'nome': 'pão', 'preco': 2.00, 'custo': 1.50, 'estoque': 100,'vendaPorDia': 19}
]

def adicionar_produto():
    nome = input("Nome do produto: ").lower()
    for p in produtos:
        if p['nome'] == nome:
            input('Produto já existe. Tente novamente.')
            return  
    preco = float(input("Preço: "))
    custo = float(input("Custo: "))
    while True:
        estoque = int(input("Estoque inicial: "))
        if estoque > 100:
            print("Erro: Não é possível adicionar mais de 100 unidades ao estoque. Tente novamente.")
            continue
        elif estoque <= 100:
            break
    vendaPorDia = int(input("Venda por dia: "))
    produtos.append({'nome': nome, 'preco': preco, 'custo': custo, 'estoque': estoque, 'vendaPorDia': vendaPorDia})
    input("Produto adicionado com sucesso. Pressione qualquer tecla.")

def remover_produto():
    produtos_ordenados = sorted(produtos, key=lambda x: x['nome'])
    print("\nProdutos:")
    for p in produtos_ordenados:
        print(f"{p['nome']} - Preço: {p['preco']} - Custo: {p['custo']} - Estoque: {p['estoque']} - Vendas por dia: {p['vendaPorDia']}")

    nome = input("Nome do produto a remover: ")
    for p in produtos:
        if p['nome'].lower() == nome.lower():
            produtos.remove(p)
            input("Produto removido.")
            return
    input("Produto não encontrado. Pressione qualquer tecla.")

def atualizar_produto():
    produtos_ordenados = sorted(produtos, key=lambda x: x['nome'])
    print("\nProdutos:")
    for p in produtos_ordenados:
        print(f"{p['nome']} - Preço: {p['preco']} - Custo: {p['custo']} - Estoque: {p['estoque']} - Vendas por dia: {p['vendaPorDia']}")

    nomeAtt = input("\nNome do produto a atualizar: ")
    for p in produtos:
        if p['nome'].lower() == nomeAtt.lower():
            opcaoDesejada = input('O que você deseja atualizar? [preço] / [custo] / [estoque] / [vendas por dia]: ').lower()
            if opcaoDesejada == 'preço':
                precoAtt = float(input('Informe o novo preço: '))
                p['preco'] = precoAtt
                input('Preço atualizado com sucesso.')
                return
            elif opcaoDesejada == 'custo':
                custoAtt = float(input('Informe o novo custo: '))
                p['custo'] = custoAtt
                input('Custo atualizado com sucesso.')
                return
            elif opcaoDesejada == 'estoque':
                estoqueAtt = int(input('Informe o novo estoque: '))
                p['estoque'] = estoqueAtt
                input('Estoque atualizado com sucesso.')
                return
            elif opcaoDesejada == 'vendas por dia':
                vendaAtt = int(input('Informe a nova quantidade de vendas por dia: '))
                p['vendaPorDia'] = vendaAtt
                input('Vendas por dia atualizado com sucesso.')
                return
            return
    input("Produto não encontrado. Pressione qualquer tecla.")

def listar_produtos():
    produtos_ordenados = sorted(produtos, key=lambda x: x['nome'])
    print("\nProdutos:")
    for p in produtos_ordenados:
        print(f"{p['nome']} - Preço: {p['preco']} - Custo: {p['custo']} - Estoque: {p['estoque']} - Vendas por dia: {p['vendaPorDia']}")
    input('\nDigite qualquer tecla.')

def produtos_mais_vendidos():
    pass
    
def previsao_falta():
    for p in produtos:
        diasRestantes =  p['estoque'] / p['vendaPorDia']
        if diasRestantes <= 3:
            input(f'O produto {p['nome']} restam {diasRestantes} dias restantes.')
        elif diasRestantes <= 0:
            input(f'O produto {p['nome']} está em falta.')

def menu_relatorios():
    while True:
        print("\n=== Relatórios ===")
        print("1. Produtos mais vendidos")
        print("2. Previsão de falta")
        print("3. Voltar")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            produtos_mais_vendidos()
        elif opcao == '2':
            previsao_falta()
        elif opcao == '3':
            break
        else:
            input("Opção inválida. Pressione qualquer tecla.")