# Produtos
from clientes import clientes

produtos = [
    {'nome': 'Arroz', 'preco': 5.50, 'custo': 4.00, 'estoque': 50},
    {'nome': 'Feijão', 'preco': 7.00, 'custo': 5.50, 'estoque': 30},
    {'nome': 'Macarrão', 'preco': 3.20, 'custo': 2.50, 'estoque': 80},
    {'nome': 'Leite', 'preco': 4.50, 'custo': 3.80, 'estoque': 20},
    {'nome': 'Pão', 'preco': 2.00, 'custo': 1.50, 'estoque': 100} 
]

def adicionar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    custo = float(input("Custo: "))
    estoque = int(input("Estoque inicial: "))
    if estoque > 100:
        print("Erro: Não é possível adicionar mais de 100 unidades de estoque.")
        return
    produtos.append({'nome': nome, 'preco': preco, 'custo': custo, 'estoque': estoque})
    print("Produto adicionado com sucesso.")


def remover_produto():
    nome = input("Nome do produto a remover: ")
    for p in produtos:
        if p['nome'].lower() == nome.lower():
            produtos.remove(p)
            print("Produto removido.")
            return
    print("Produto não encontrado.")

def listar_produtos():
    produtos_ordenados = sorted(produtos, key=lambda x: x['nome'])
    print("\nProdutos:")
    for p in produtos_ordenados:
        print(f"{p['nome']} - Preço: {p['preco']}, Estoque: {p['estoque']}")

def listar_clientes():
    clientes_ordenados = sorted(clientes, key=lambda x: x['nome'])
    print("\nClientes:")
    for c in clientes_ordenados:
        print(f"{c['nome']} - CPF: {c['cpf']}")

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
            print("Opção inválida.")