'''
Cenário 6 - Supermercado com Estoque e Previsão de Vendas

User Story: Como gestor do supermercado, quero controlar estoque e vendas, para prever falta
de produtos.
Contexto: Produtos acabam rapidamente sem previsão, gerando insatisfação de clientes.
Problema: Não há cálculo de reposição automática de estoque.
Estruturas Operacionais:
- CRUD de produtos, clientes e vendas.
- Atualização automática do estoque.
- Cálculo de margem de lucro.
- Relatório de produtos mais vendidos.
- Previsão de falta de produtos.
Atividades Propostas:
- A. CRUD de produtos e clientes.
- B. Atualizar estoque após cada venda.
- C. Calcular lucro por produto.
- D. Relatório de produtos mais vendidos.
- E. Relatório de previsão de falta.
'''

import os; import time


usuarioCheck = "0"; senhaCheck = "0"
clientes = []; produtos = []
estoqueMax = 100

def limparTela():
    os.system('cls')

def adicionarEstoque():
    limparTela()
    print('_+=+=+=+=+=+=+=+=+=+=+=+=_')
    print('| ADICIONANDO AO ESTOQUE |')
    print('*+=+=+=+=+=+=+=+=+=+=+=+=*')
    while True:   
        try:
            numProdutos = int(input('Quantos produtos você deseja cadastrar? '))
        except ValueError:
            input('Digite um número válido. Pressione qualquer tecla para continuar.')
            limparTela()
            continue
        else:
            for _ in range(numProdutos):
                nome = input("Informe o nome do produto: ").lower().strip()
                
                encontrado = False
                for item in produtos:
                    if item["produto"] == nome:
                        qnt = int(input(f"O produto '{nome}' já existe! Informe a quantidade a ser adicionada: "))
                        if (item['quantidade'] + qnt) < 100:
                            item["quantidade"] += qnt
                            print(f"Estoque atualizado: {item['quantidade']} unidades de {nome}.")
                            print('*+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=*')
                            input('Pressione qualquer tecla para continuar.')
                            encontrado = True
                            break
                        else:
                            print(f'O estoque atual de {item['produto']} é de {item['quantidade']}. Valor máximo determinado: {estoqueMax} unidades.')
                            print('*+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=*')
                            input('Pressione qualquer tecla para continuar.')
                            encontrado = True
                            break
                if encontrado == False:                                  
                # Ou poderiamos usar [if not encontrado], daria no mesmo
                    while True:
                        try:    
                            qntProduto = int(input("Informe a quantidade do produto: "))
                            custoProduto = float(input("Informe o custo do produto: "))
                            valorVenda = float(input("Informe o valor de venda: "))
                            break
                        except:
                            input('Digite um número válido. Pressione qualquer tecla para continuar.')
                            continue

                    novoProduto = {
                        "produto": nome,
                        "quantidade": qntProduto,
                        "custo": custoProduto,
                        "valordevenda": valorVenda
                    } 

                    produtos.append(novoProduto)
                    print("=+"*20)
                    print("Produto adicionado com sucesso.")
                    print("=+"*20)
                    time.sleep(1.5)
            break

def removendoEstoque():
    limparTela()
    print('_+=+=+=+=+=+=+=+=+=+=+=+=_')
    print('|  REMOVENDO DO ESTOQUE  |')
    print('*+=+=+=+=+=+=+=+=+=+=+=+=*')

    print("\nEstoque inicial:")
    for p in produtos:
        print(p)

    print('*+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=*')
    nome = input("Qual produto deseja remover? ")
    qtd = int(input("Quantas unidades deseja remover? "))
    for item in produtos:
        if item["produto"] == nome.lower().strip():
            if qtd >= item["quantidade"]:
                produtos.remove(item)
                print(f"Produto '{nome}' removido do estoque. Zero unidades restantes.")
            else:
                item["quantidade"] -= qtd
                print(f"Removido {qtd} unidades de '{nome}'. Agora restam {item['quantidade']} unidades.")

    print("\nEstoque final: ")
    for p in produtos:
        print(p)

    input("*")

def olharEstoque():
    limparTela()
    print('_+=+=+=+=+=+=+=+=+=+=+=+_')
    print('|  ESTOQUE DE PRODUTOS  |')
    print('*+=+=+=+=+=+=+=+=+=+=+=+*')
    for p in produtos:
        print("       |       ".join(p))
        print(f'{p['produto']:^14}| {p['quantidade']:^23}| {p['custo']:^18.2f}| {p['valordevenda']:^21.2f}')
        print('=+'*40)

    input('\nPressione qualquer tecla para continuar.')

while True:
    limparTela()
    print('_+=+=+=+=+=+=+=+=+=_')
    print('|   AUTENTICAÇÃO   |')
    print('*+=+=+=+=+=+=+=+=+=*')
    print('|[1] Cliente       |')
    print('|[2] Gerente       |')
    print('|[3] Sair          |')
    print('*+=+=+=+=+=+=+=+=+=*\n')
    try:
        selecao = int(input('Selecionar: '))
    except ValueError:
        input('Digite um número válido. Pressione qualquer tecla para continuar.')
        limparTela()
        continue
    else:
        match selecao:
            case 1:
                while True:
                    limparTela()
                    print('_+=+=+=+=+=+=+=+=+=+=+=_')
                    print('|     MENU CLIENTE     |')
                    print('*+=+=+=+=+=+=+=+=+=+=+=*')
                    print('[1] Cadastrar conta    |')
                    print('[2] Comprar produto    |')
                    print('[3] Menu Principal     |')
                    print('*+=+=+=+=+=+=+=+=+=+=+=*\n')
                    try:
                        selecao = int(input('Selecionar: '))
                    except ValueError:
                        input('Digite um número válido. Pressione qualquer tecla para continuar.')
                        limparTela()
                        continue
                    else:
                         match selecao:
                              case 1: 
                                limparTela()
                                print('_+=+=+=+=+=+=+=+=+=+=+=+_')
                                print('|  CADASTRANDO USUÁRIO  |')
                                print('*+=+=+=+=+=+=+=+=+=+=+=+*')
                                while True:   
                                    try:
                                        nomeCliente = input('Informe o seu nome: ')
                                        if nomeCliente.isnumeric():
                                            print('Inválido. Tente novamente.')
                                            raise ValueError
                                        else:
                                            try:
                                                idadeCliente = int(input('Informe a sua idade: '))
                                            except ValueError:
                                                input('Informe uma idade válida.')
                                                continue
                                            else:
                                                enderecoCliente = input('Informe seu endereço: ')
                                                try:
                                                    numCasa = int(input('Informe o nº da casa: '))
                                                except ValueError:
                                                    input('Informe um número válido.')
                                                    continue
                                                else:
                                                    encontradoCliente = False
                                                    for cliente in clientes:
                                                        if cliente["nome"] == nomeCliente:
                                                            input(f"O cliente '{nomeCliente}' já existe! Tente novamente.")
                                                            print('=+'*20)
                                                            input('Pressione qualquer tecla para continuar.')
                                                            encontradoCliente = True
                                                            break

                                                    if encontradoCliente == False:                                  
                                                    # Ou poderiamos usar [if not encontradoCliente], daria no mesmo
                                                        novoCliente = {
                                                            "nome": nomeCliente,
                                                            "idade": idadeCliente,
                                                            "endereço": enderecoCliente,
                                                            "número da casa": numCasa
                                                        } 

                                                        clientes.append(novoCliente)
                                                        print("=+"*20)
                                                        print("Cliente cadastrado com sucesso.")
                                                        print("=+"*20)
                                                        time.sleep(1.5)
                                            break
                                    except ValueError:
                                        input('Digite um nome válido. Pressione qualquer tecla para continuar.')
                                        limparTela()
                                        continue                                          
                              case 2: pass
                              case 3: break                           
            case 2:
                while True:
                    limparTela()
                    print('_+=+=+=+=+=+=+=+=+=+_')
                    print('|    LOGIN ADMIN    |')
                    print('*+=+=+=+=+=+=+=+=+=+*')
                    usuario = input('Digite o usuário (ou sair): ')
                    if usuario == 'sair':
                        break

                    senha = input('Digite a senha: ')
                    if senha != senhaCheck or usuario != usuarioCheck:
                        input('Usuário ou Senha inválidos. Tente novamente.')
                        continue
                    elif usuario == usuarioCheck and senha == senhaCheck:
                        print('Login realizado com sucesso.')
                        time.sleep(1)  
                    
                        while True:
                            limparTela()
                            print('_+=+=+=+=+=+=+=+=+=+=+=+=_')
                            print('|      MENU GERÊNCIA     |')
                            print('*+=+=+=+=+=+=+=+=+=+=+=+=*')
                            print('|[1] Gerir estoque       |')
                            print('|[2] Listar clientes     |')
                            print('|[3] Analisar relatórios |')
                            print('|[4] Sair                |')
                            print('*+=+=+=+=+=+=+=+=+=+=+=+=*\n')
                            try:
                                selecao = int(input('Selecionar: '))
                            except ValueError:
                                input('Digite um número válido. Pressione qualquer tecla para continuar.')
                                limparTela()
                                continue
                            else:
                                match selecao:
                                    case 1:
                                        while True:
                                            limparTela()
                                            print('_+=+=+=+=+=+=+=+=+=+_')
                                            print('|   GERIR ESTOQUE   |')
                                            print('*+=+=+=+=+=+=+=+=+=+*')
                                            print('|[1] Adicionar      |')
                                            print('|[2] Remover        |')
                                            print('|[3] Listar         |')
                                            print('|[4] Voltar         |')
                                            print('*+=+=+=+=+=+=+=+=+=+*')
                                            try:
                                                selecao = int(input('Selecionar: '))
                                            except ValueError:
                                                input('Digite um número válido. Pressione qualquer tecla para continuar.')
                                                continue
                                            else:
                                                match selecao:
                                                    case 1: 
                                                        adicionarEstoque()
                                                    case 2: 
                                                        removendoEstoque()
                                                    case 3: 
                                                        olharEstoque()
                                                    case 4: break
                                    case 2:
                                        limparTela()
                                        print('_+=+=+=+=+=+=+=+=+=+=+=+=_')
                                        print('|  CLIENTES CADASTRADOS  |')
                                        print('*+=+=+=+=+=+=+=+=+=+=+=+=*')
                                        for c in clientes:
                                            print('|       nome       |   idade   |            endereço            |  Nº  |')
                                            # print("            |           ".join(c))
                                            print(f'|{c['nome']:^18}| {c['idade']:^10}| {c['endereço']:^31}|{c['número da casa']:^6}|')
                                            print('=+'*36)

                                        input('\nPressione qualquer tecla para continuar.')
                                        input('*')
                                    case 3:
                                        while True:
                                            limparTela()
                                            print('_+=+=+=+=+=+=+=+=+=+=+=+=+=_')
                                            print('|        RELATÓRIOS        |')
                                            print('*+=+=+=+=+=+=+=+=+=+=+=+=+=*')
                                            print('|[1] Produtos mais vendidos|')
                                            print('|[2] Previsão de falta     |')
                                            print('|[3] Menu Principal        |')
                                            print('*+=+=+=+=+=+=+=+=+=+=+=+=+=*')
                                            try:
                                                selecao = int(input('Selecionar: '))
                                            except ValueError:
                                                input('Digite um número válido. Pressione qualquer tecla para continuar.')
                                                continue
                                            else:
                                                match selecao:
                                                    case 1: 
                                                        pass
                                                    case 2: 
                                                        pass
                                                    case 3: 
                                                        break
                                                    case _: 
                                                        input('Digite um número válido. Pressione qualquer tecla para continuar.')
                                                        continue
                                    case 4: 
                                        print('Encerrando o menu. Obrigado pela utilização.'); time.sleep(2); limparTela(); break
                                    case _:
                                        input('Digite um número válido. Pressione qualquer tecla para continuar.')
                                        continue
            case 3: 
                print('Encerrando o programa. Obrigado pela utilização.'); 
                time.sleep(2) 
                limparTela() 
                break
            case _:
                input('Digite um número válido. Pressione qualquer tecla para continuar.')
                continue
   

# while True:
#                             limparTela()
#                             print('_+=+=+=+=+=+=+=+=+=+_')
#                             print('|   MENU DE COMPRA   |')
#                             print('*+=+=+=+=+=+=+=+=+=+*')
#                             print('[1] Cadastro de cliente')
#                             print('[2] Lista de produtos')
#                             print('[3] Menu Principal')
#                             try:
#                                 selecao = int(input('Selecionar: '))
#                             except ValueError:
#                                 input('Digite um número válido. Pressione qualquer tecla para continuar.')
#                                 continue
#                             else:
#                                 match selecao:
#                                     case 1: 
#                                         pass
#                                     case 1: 
#                                         pass
#                                     case 1: 
#                                         pass
#                                     case 4: break 