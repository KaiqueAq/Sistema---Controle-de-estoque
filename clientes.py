#Cadastramento
import os
import produto as pd, funcionarios as fc, datetime, limparTela as lt, vendas as vd, time

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
    clientes_ordenados = sorted(clientes, key=lambda x: x['nome'])
    print('_=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=_')
    print('|         LISTA DE CLIENTES DO MERCADO ATUALIZADA           |')
    print('*-----------------------------------------------------------*\n')
    print(' ___________________________________________________________ ')
    print('|             Nome              |  idade  |       CPF       |')
    print('*-----------------------------------------------------------*')
    for i in clientes_ordenados:
        print(f"|{i['nome']:<31}|{i['idade']:>3} anos |{i['cpf']:<17}|")
    print('*-----------------------------------------------------------*')
    input('\nPressione qualquer tecla.')

def remover_cliente():
    nome_remover = input("Digite o nome do cliente a ser removido: "). upper()
    for cliente in clientes:
        if cliente['nome'] == nome_remover:
            clientes.remove(cliente)
            print(f"\n Cliente {nome_remover} removido com sucesso!")
            return
    print(f"\n Cliente {nome_remover} não encontrado.")

def comprarProduto():
    try:
        qntsProdutos = int(input('Quantos produtos diferentes deseja comprar? '))
    except ValueError:
        input("Entrada inválida. Por favor, digite um número. Pressione qualquer tecla para continuar.")
    else:
        for i in range(qntsProdutos):

            print("\nProdutos:")
            pd.produtos.sort(key=lambda x:x['nome'])
            for p in pd.produtos:
                print(f"{p['nome']} - Preço: {p['preco']} - Estoque: {p['estoque']}")
            qualProduto = input(f'\n({i+1}/{qntsProdutos}): Qual produto deseja comprar? ').lower() 

            pdEncontrado = None

            # Procura o produto na nossa lista de na outra página produto.py
            for p in pd.produtos:
                if p['nome'] == qualProduto:
                    pdEncontrado = p
                    break

            # Se após o for a gente não achar o produto, a parece uma mensagem e já vai pro próximo item do for
            if pdEncontrado == None:
                input(f'Produto "{qualProduto}" não encontrado. Pressione qualquer tecla para continuar.')
                continue

            # Se achar o produto ele pede a quantidade
            qualQntd = int(input(f'Informe a quantidade de {qualProduto} desejada: '))
            
            if qualQntd <= 0:
                print("Quantidade inválida.")
                continue

            # Se a quantidade for maior que o estoque do produto pedido, manda uma mensagemd e erro
            if qualQntd > pdEncontrado['estoque']:
                print(f'Estoque não supre o pedido. Temos apenas {pdEncontrado["estoque"]} unidades.')
                continue
            else:
                # Se não for, diminui do estoque
                pdEncontrado['estoque'] -= qualQntd
                
            # Calcula o subTotal e o lucro do item
            subTotal = pdEncontrado['preco'] * qualQntd
            lucroItem = pdEncontrado['lucro'] * qualQntd

            if pdEncontrado['estoque'] == 0:
                # O .remove() modifica a lista diretamente. Não precisa atribuir a uma variável.
                pd.produtos.remove(pdEncontrado)
                print(f'Adicionado ao carrinho. Estoque de {qualProduto} zerado. Produto removido do sistema.')
            else:
                print(f'Adicionado ao carrinho. Estoque restante: {pdEncontrado["estoque"]} unidades.')

            # Adiciona o item ao nosso carrinho temporário
            vd.carrinhoDeCompra.append({
                'nome': qualProduto,
                'quantidade': qualQntd,
                'subTotal': subTotal
            })
            
            # Atualiza os totais da venda
            vd.totalDeVenda += subTotal
            vd.lucroDaVenda += lucroItem
        
        # DEPOIS que o loop terminar, se o carrinho não estiver vazio, finalize a venda
            if vd.carrinhoDeCompra:
                # Pega o CPF do cliente (poderia ser feito no início)
                cpfCliente = input("\nInforme o seu CPF (opcional): ")
                if cpfCliente:
                    cpfCliente = cpfCliente
                else:
                    cpfCliente = 'Não informado'
                
            # Cria o dicionário da nova venda com os dados acumulados
                nova_venda = {
                    'cliente_cpf': cpfCliente,
                    'produtos': vd.carrinhoDeCompra,
                    'total': vd.totalDeVenda,
                    'lucro': vd.lucroDaVenda,
                    'data': datetime.date.today().isoformat() # Pega a data atual
                }

                # Adiciona a venda finalizada na lista principal
                vd.vendas.append(nova_venda)
                os.system('cls')
                print("\nA compra foi realizada com Sucesso!")
                print(f"\nCPF do Cliente: {nova_venda['cliente_cpf']}")
                print("\nProdutos Comprados:\n")
                print('|  produto  | Quantidade | Subtotal |')
                for item in nova_venda['produtos']:               
                    print(f"|{item['nome']:^11}|{item['quantidade']:^12}| R${item['subTotal']:<7.2f}|")
                input(f"\nTOTAL DA VENDA: R${nova_venda['total']:.2f}")
                lt.limpaTela()
            else:
                input("\nNenhum produto foi adicionado ao carrinho. Compra não realizada. Pressione qualquer tecla.")
        vd.carrinhoDeCompra = [] 
        vd.totalDeVenda = 0 
        vd.lucroDaVenda = 0

   
    #     qntsProdutos = int(input('Quantos produtos diferentes deseja comprar? '))
    # except ValueError:
    #     input("Entrada inválida. Por favor, digite um número. Pressione qualquer tecla para continuar.")
    # else:
    #     venda_realizada = False

    #     for i in range(qntsProdutos):
    #         print("\nProdutos Disponíveis:")
    #         # É uma boa prática mostrar a lista atualizada a cada iteração
    #         for p in pd.produtosOrdenados: # Supondo que esta seja sua lista principal
    #             print(f"- {p['nome'].title()} | Preço: R${p['preco']:.2f} | Estoque: {p['estoque']}")
            
    #         qualProduto = input(f'\n({i+1}/{qntsProdutos}): Qual produto deseja comprar? ').lower().strip()

    #         pdEncontrado = None
    #         # Procura o produto na lista
    #         for p in pd.produtosOrdenados:
    #             if p['nome'] == qualProduto:
    #                 pdEncontrado = p
    #                 break

    #         if not pdEncontrado:
    #             input(f'Produto "{qualProduto}" não encontrado. Pressione qualquer tecla para continuar.')
    #             continue

    #         try:
    #             qualQntd = int(input(f'Informe a quantidade de "{qualProduto}" desejada: '))
    #         except ValueError:
    #             print("Quantidade inválida. Digite um número.")
    #             continue
            
    #         if qualQntd <= 0:
    #             print("Quantidade deve ser maior que zero.")
    #             continue

    #         # 1. Verifica se tem estoque suficiente
    #         if qualQntd > pdEncontrado['estoque']:
    #             print(f'Estoque não supre o pedido. Temos apenas {pdEncontrado["estoque"]} unidades.')
    #         else:
    #             # 2. Se tem estoque, a venda acontece. Processa os dados.
    #             venda_realizada = True # Marca que pelo menos um item foi adicionado
                
    #             # Calcula o subTotal e o lucro do item
    #             subTotal = pdEncontrado['preco'] * qualQntd
    #             lucroItem = pdEncontrado['lucro'] * qualQntd

    #             # Adiciona o item ao carrinho
    #             vd.carrinhoDeCompra.append({
    #                 'nome': qualProduto,
    #                 'quantidade': qualQntd,
    #                 'subTotal': subTotal
    #             })
                
    #             # Atualiza os totais da venda
    #             vd.totalDeVenda += subTotal
    #             vd.lucroDaVenda += lucroItem

    #             # ATUALIZA O ESTOQUE
    #             pdEncontrado['estoque'] -= qualQntd
                
    #             print(f'"{qualProduto}" foi adicionado ao carrinho.')

    #             # 3. AGORA, verifica se o estoque zerou para remover o produto
                


                

    #         # DEPOIS que o loop terminar, se o carrinho não estiver vazio, finalize a venda
    #         if venda_realizada:
    #             # Pega o CPF do cliente
    #             if vd.carrinhoDeCompra:
    #                 cpfCliente = input("\nInforme o seu CPF: (opcional)")
    #                 if cpfCliente:
    #                     cpfCliente = cpfCliente
    #                 else:
    #                     cpfCliente = None

    #             # Cria o dicionário da nova venda com os dados acumulados
    #             nova_venda = {
    #                 'cliente_cpf': cpfCliente,
    #                 'produtos': vd.carrinhoDeCompra,
    #                 'total': vd.totalDeVenda,
    #                 'lucro': vd.lucroDaVenda,
    #                 'data': datetime.date.today().isoformat()
    #             }

    #             # Adiciona a venda finalizada à sua lista principal
    #             vd.vendas.append(nova_venda)
                
    #             # Limpa o carrinho e totais para a próxima venda
    #             # vd.carrinhoDeCompra.clear()
    #             # vd.totalDeVenda = 0.0
    #             # vd.lucroDaVenda = 0.0
                
    #             os.system('cls')
    #             print("\n--- Compra Realizada com Sucesso! ---")
    #             print(f"CPF do Cliente: {nova_venda['cliente_cpf']}")
    #             print("Produtos Comprados:")
    #             for item in nova_venda['produtos']:
    #                 print(f"  - {item['nome']}, Quantidade: {item['quantidade']}, Subtotal: R${item['subTotal']:.2f}")
    #             input(f"\nTOTAL DA VENDA: R${nova_venda['total']:.2f}\n\nPressione Enter para continuar...")
    #             # lt.limpaTela()
    #         else:
    #             print("\nNenhum produto foi adicionado ao carrinho. Compra não realizada.")
