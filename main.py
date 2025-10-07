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
from limparTela import limpaTela
import produto, clientes, funcionarios as fc, gerente as gt, vendas as vd, os, time

# Vai ter um menu que seleciona gerente ou cliente e sair
while True:
    try:
        limpaTela()
        print('_=+=+=+=+=+=+=+=+=+=+_')
        print('| SISTEMA DE MERCADO |')
        print('*--------------------*')
        print('|[1] Cliente         |')
        print('|[2] Funcionário     |')
        print('|[3] Gerente         |')
        print('|[4] Sair            |')
        print('*=+=+=+=+=+=+=+=+=+=+*')
        opcao = int(input('Digite a opção desejada: '))
    except ValueError:
        input('Digite uma opção válida.')
        continue
    else:
        match opcao:
            case 1:
                while True:
                    limpaTela()
                    print('_=+=+=+=+=+=+=+_')
                    print('| MENU CLIENTE |')
                    print('*--------------*')
                    print('|[1] Comprar   |')
                    print('|[2] Voltar    |')
                    print('*=+=+=+=+=+=+=+*')
                    try:
                        opcao = int(input('Digite a opção desejada: '))
                    except ValueError:
                        input('Opção inválida. Pressione qualquer tecla para continuar.')
                        continue
                    else:
                        match opcao:
                            case 1:
                                limpaTela()
                                clientes.comprarProduto()
                            case 2:
                                limpaTela()
                                break
                            case _: 
                                input('Opção inválida. Pressione qualquer tecla para continuar.')
                                continue
            case 2:  
                rodando = True
                while rodando:
                    limpaTela()
                    print(' ----------------')
                    print('|   Menu Login   |')
                    print('*----------------*')
                    usuario = input('- Usuário (ou sair): ')
                    if usuario == 'sair':
                        break
                    senha = input('- Senha: ')
                    logou = False
                    for funcionario in fc.funcionarios:
                        if funcionario['nome'] == usuario and funcionario['senha'] == senha:
                            input(f'\nOlá {usuario}. Login realizado com sucesso.\nEntrando no sistema...')
                            logou = True
                            while True:
                                limpaTela()
                                print('_=+=+=+=+=+=+=+=+=+=+=+_')
                                print('|   Menu Funcionário   |')
                                print('*----------------------*')
                                print('|[1] Adicionar produto |')
                                print('|[2] Listar produtos   |')
                                print('|[3] Remover produto   |')
                                print('|[4] Listar clientes   |')
                                print('|[5] Logout            |')
                                print('*=+=+=+=+=+=+=+=+=+=+=+*')
                                try:
                                    opcao = int(input('Digite a opção desejada: '))
                                except ValueError:
                                    input('Digite uma opção válida.')
                                    continue
                                else:
                                    match opcao:
                                        case 1:
                                            limpaTela()
                                            produto.adicionar_produto()
                                        case 2:
                                            limpaTela()
                                            produto.listar_produtos()
                                        case 3:
                                            limpaTela()
                                            produto.remover_produto()
                                        case 4:
                                            limpaTela()
                                            clientes.listar_clientes(clientes.clientes)
                                        case 5:
                                            rodando = False
                                            break
                                        case _:
                                            input('Opção inválida. Pressione qualquer tecla para continuar.')
                                            continue
                    if logou == False:
                        input('\nLogin inválido. Pressione qualquer tecla para continuar.')
                        limpaTela()
                        continue   
            case 3:
                rodando = True
                while rodando:
                    limpaTela()
                    print(' ----------------')
                    print('|   Menu Login   |')
                    print('*----------------*')
                    usuario = input('- Usuário (ou sair): ')
                    if usuario == 'sair':
                        break
                    senha = input('- Senha: ')
                    logou = False
                    for gerente in gt.gerenteConta:
                        if gerente['nome'] == usuario and gerente['senha'] == senha:
                            input(f'\nOlá {usuario}. Login realizado com sucesso.\nEntrando no sistema...')
                            logou = True
                            while True:
                                limpaTela()
                                print('_=+=+=+=+=+=+=+=+=+=+=+=+=+_')
                                print('|       Menu Gerente       |')
                                print('*--------------------------*')
                                print('|[1] Atualizar produto     |')
                                print('|[2] Listar funcionários   |')
                                print('|[3] Atualizar funcionários|')
                                print('|[4] Relatórios            |')
                                print('|[5] Logout                |')
                                print('*=+=+=+=+=+=+=+=+=+=+=+=+=+*')
                                try:
                                    opcao = int(input('Digite a opção desejada: '))
                                except ValueError:
                                    input('Digite uma opção válida.')
                                    continue
                                else:
                                    match opcao:
                                        case 1:
                                            limpaTela()
                                            produto.atualizar_produto()
                                        case 2:
                                            limpaTela()
                                            fc.listar_funcionarios(fc.funcionarios)
                                        case 3:
                                            gt.atualizar_funcionarios(gt.funcionarios)
                                        case 4:
                                            limpaTela()
                                            produto.menu_relatorios()
                                        case 5:
                                            rodando = False
                                            break
                                        case _:
                                            input('Opção inválida. Pressione qualquer tecla para continuar.')
                                            continue
                    if logou == False:
                        input('\nLogin inválido. Pressione qualquer tecla para continuar.')
                        limpaTela()
                        continue  
            case 4:
                print('\nSaindo do programa...')
                time.sleep(2)
                break
            case _:
                input('Opção inválida. Pressione qualquer tecla para continuar.')
                continue

# Menu de Gerente vai ter
    # Adicionar
        #Se o gerente quiser adicionar acima de 100, dá mensagem de erro
    # remover
    # Listar Produtos  (ordem alfabetica) 
    # Listar Clientes (ordem alfabetica)  
    # Relatórios
        #Produtos mais vendidos
        #Previsão de falta      
    # Voltar
    
# Menu de CLiente vai ter
    # Cadastrar
    # Comprar
        # Cliente quiser comprar a mais do Estoque
    # Ver catálogo
    # Voltar



