#Estoque
import vendas as vd, os, json, clientes as cl

estoqueMax = 100

# produtosOrdenados = sorted(produtos, key=lambda x:x['nome'])
# produtosOrdemPeloCod = sorted(produtosOrdenados, key=lambda x:x['codigo'])

def gerar_codigo():
    produtos = cl.dados.get('produtos', [])
    if len(produtos) == 0:
        return 1
    else:
        return max(p['codigo'] for p in produtos) + 1

def adicionar_produto():
    produtos = cl.dados.get('produtos', [])
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
        elif estoque == 0:
            print("Erro: Não é possível adicionar estoque vazio. Tente novamente.")
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

    cl.save_dados()  # Salva imediatamente após adicionar
    input(f"Produto adicionado com sucesso! Código do produto: {codigo}. Pressione qualquer tecla.")

def remover_produto():
    produtos = cl.dados.get('produtos', [])
    listar_produtos_att()
    codigo = int(input("\nDigite o código do produto a remover: "))
    for p in produtos:
        if p['codigo'] == codigo:
            produtos.remove(p)
            input("Produto removido com sucesso.")
            return
    input("Produto não encontrado. Pressione qualquer tecla.")

def atualizar_produto():
    produtos = cl.dados.get('produtos', [])
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
    produtos = cl.dados.get('produtos', [])
    print('Produtos:')
    print(' ____________________________________________________________________________')
    print('| Cod |       Nome       |  Preço  |  Custo  |  Lucro  | Estoque | Venda/dia |')
    for p in produtos:
        print(f"|{p['codigo']:^5}|{p['nome']:<18}| R${p['preco']:<5.2f} | R${p['custo']:<5.2f} | R${p['lucro']:<5.2f} |{p['estoque']:>6}   | {p['vendaPorDia']:>6}    |")
    print('*============================================================================*')
    input('\nPressione qualquer tecla para continuar.')

def ver_produtos():
    produtos = cl.dados.get('produtos', [])
    produtosOrdemNome = sorted(produtos, key=lambda x:x['nome'])
    print('Produtos:')
    for p in produtosOrdemNome:
        print(f"{p['nome']} - Preço: {p['preco']} - Estoque: {p['estoque']}")

def listar_produtos_att():
    produtos = cl.dados.get('produtos', [])
    print("Atualizando produtos:")
    print('_______________________________________________________________________________')
    print('| Cod |       Nome       |  Preço  |  Custo  |  Lucro  | Estoque | Vendas/dia |')
    for p in produtos:
        print(f"|{p['codigo']:^5}|{p['nome']:^18}| R${p['preco']:<5.2f} | R${p['custo']:<5.2f} | R${p['lucro']:<5.2f} |{p['estoque']:^9}|{p['vendaPorDia']:^12}|")
    print('===============================================================================')

def menu_relatorios():
    produtos = cl.dados.get('produtos', [])
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
