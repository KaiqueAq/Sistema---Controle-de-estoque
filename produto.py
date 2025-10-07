#Estoque
import vendas as vd, os

estoqueMax = 100

produtos = [
    {'codigo': 1, 'nome': 'arroz', 'preco': 5.50, 'custo': 4.00, 'lucro': 1.50, 'estoque': 50, 'vendaPorDia': 10},
    {'codigo': 2, 'nome': 'feijão', 'preco': 7.00, 'custo': 5.50, 'lucro': 1.50, 'estoque': 30, 'vendaPorDia': 15},
    {'codigo': 3, 'nome': 'macarrão', 'preco': 3.20, 'custo': 2.50, 'lucro': 0.70, 'estoque': 80, 'vendaPorDia': 13},
    {'codigo': 4, 'nome': 'leite', 'preco': 4.50, 'custo': 3.80, 'lucro': 0.70, 'estoque': 20, 'vendaPorDia': 8},
    {'codigo': 5, 'nome': 'pão', 'preco': 2.00, 'custo': 1.50, 'lucro': 0.50, 'estoque': 100, 'vendaPorDia': 19}
]
produtos.sort(key=lambda x:x['codigo'])
# produtosOrdenados = sorted(produtos, key=lambda x:x['nome'])
# produtosOrdemPeloCod = sorted(produtosOrdenados, key=lambda x:x['codigo'])

def gerar_codigo():
    if len(produtos) == 0:
        return 1
    else:
        return max(p['codigo'] for p in produtos) + 1
    
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
        else:
            break

    vendaPorDia = int(input("Venda por dia: "))
    
    codigo = gerar_codigo() 

    produtos.append({
        'codigo': codigo,
        'nome': nome,
        'preco': preco,
        'custo': custo,
        'lucro': (preco - custo),
        'estoque': estoque,
        'vendaPorDia': vendaPorDia
    })
    
    input(f"Produto adicionado com sucesso! Código do produto: {codigo}. Pressione qualquer tecla.")

def remover_produto():
    listar_produtos_att()
    codigo = int(input("\nDigite o código do produto a remover: "))
    for p in produtos:
        if p['codigo'] == codigo:
            produtos.remove(p)
            input("Produto removido com sucesso.")
            return
    input("Produto não encontrado. Pressione qualquer tecla.")

def atualizar_produto():
    listar_produtos_att()
    codigo = input("\nDigite o código do produto a atualizar (ou sair): ")
    if codigo == 'sair':
        return
    elif codigo.isnumeric():
        codigo = int(codigo)
    for p in produtos:
        if p['codigo'] == codigo:
            opcaoDesejada = input('O que deseja atualizar? [preço] / [custo] / [estoque] / [vendas por dia]: ').lower()
            if opcaoDesejada == 'preço':
                p['preco'] = float(input('Novo preço: '))
                input('Preço atualizado com sucesso.')
            elif opcaoDesejada == 'custo':
                p['custo'] = float(input('Novo custo: '))
                input('Custo atualizado com sucesso.')
            elif opcaoDesejada == 'estoque':
                novo_estoque = int(input('Novo estoque: '))
                if novo_estoque > 100:
                    input(f'Estoque excede o limite de {estoqueMax}.')
                else:
                    p['estoque'] = novo_estoque
                    input('Estoque atualizado com sucesso.')
            elif opcaoDesejada == 'vendas por dia':
                p['vendaPorDia'] = int(input('Nova venda por dia: '))
                input('Vendas por dia atualizadas com sucesso.')
            return
    input("Produto não encontrado. Pressione qualquer tecla.")

def listar_produtos():
    print('Produtos:')
    print('______________________________________________________________________________')
    print('| Cod |       Nome       |  Preço  |  Custo  |  Lucro  | Estoque | Venda/dia |')
    for p in produtos:
        print(f"|{p['codigo']:^5}|{p['nome']:^18}| R${p['preco']:<5.2f} | R${p['custo']:<5.2f} | R${p['lucro']:<5.2f} |{p['estoque']:^9}|{p['vendaPorDia']:^11}|")
    print('==============================================================================')
    input('\nPressione qualquer tecla para continuar.')
        
def ver_produtos():
    produtosOrdemNome = sorted(produtos, key=lambda x:x['nome'])
    print('Produtos:')
    for p in produtosOrdemNome:
        print(f"{p['nome']} - Preço: {p['preco']} - Estoque: {p['estoque']}")

def listar_produtos_att():
    print("Atualizando produtos:")
    print('_______________________________________________________________________________')
    print('| Cod |       Nome       |  Preço  |  Custo  |  Lucro  | Estoque | Vendas/dia |')
    for p in produtos:
        print(f"|{p['codigo']:^5}|{p['nome']:^18}| R${p['preco']:<5.2f} | R${p['custo']:<5.2f} | R${p['lucro']:<5.2f} |{p['estoque']:^9}|{p['vendaPorDia']:^12}|")
    print('===============================================================================')



def menu_relatorios():
    while True:
        os.system('cls')
        print('_=+=+=+=+=+=+=+=+=+=+=+=+=+_')
        print('|        RELATÓRIOS        |')
        print('*--------------------------*')
        print('|[1] Produtos mais vendidos|')
        print('|[2] Previsão de falta     |')
        print('|[3] Voltar                |')
        print('*=+=+=+=+=+=+=+=+=+=+=+=+=+*')
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            vd.maisVendidos(produtos)
        elif opcao == '2':
            vd.previsaoFalta(produtos)
        elif opcao == '3':
            break
        else:
            input("Opção inválida. Pressione qualquer tecla.")

# def produtos_mais_vendidos():
#     pass
    
# def previsao_falta():
#     for p in produtos:
#         diasRestantes =  p['estoque'] / p['vendaPorDia']
#         if diasRestantes <= 3:
#             print(f'O produto {p['nome']} restam {diasRestantes} dias restantes.')
#         elif diasRestantes <= 0:
#             print(f'O produto {p['nome']} está em falta.')
#     input('Pressione qualquer tecla para continuar.')

