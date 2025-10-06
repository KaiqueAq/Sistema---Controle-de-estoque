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
import produto, clientes, vendas, funcionarios as fc

# Vai ter um menu que seleciona gerente ou cliente e sair
while True:
    try:
        limpaTela()
        opcao = int(input('Digite [1] se você é Cliente\nDigite [2] se você é funcionário\nDigite [3] se você é Gerente\n[4] Sair.\n'))
    except ValueError:
        input('Digite uma opção válida.')
        continue
    else:
        match opcao:
            case 1:
                while True:
                    limpaTela()
                    print('Menu Cliente')
                    print('[1] Comprar')
                    print('[2] Voltar')
                    try:
                        opcao = int(input('Digite a opção desejada: '))
                    except ValueError:
                        input('Opção inválida. Pressione qualquer tecla para continuar.')
                        continue
                    else:
                        match opcao:
                            case 1:
                                limpaTela()
                                print('Menu Compra') 
                                clientes.comprarProduto()
                            case 2:
                                limpaTela()
                                print('Voltar')
                                break
                            case _: 
                                input('Opção inválida. Pressione qualquer tecla para continuar.')
                                continue
            case 2:  
                rodando = True
                while rodando:
                    usuario = input('Usuário (ou sair): ')
                    if usuario == 'sair':
                        break
                    senha = input('Senha: ')
                    logou = False
                    for funcionario in fc.funcionarios:
                        if funcionario['nome'] == usuario and funcionario['senha'] == senha:
                            input(f'Olá {usuario}. Login realizado com sucesso.\n')
                            logou = True
                            while True:
                                limpaTela()
                                print('Menu Funcionário')
                                print('[1] Adicionar produto')
                                print('[2] Listar produtos')
                                print('[3] Remover produto')
                                print('[4] Listar clientes')
                                print('[5] Voltar')
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
                                            break
                                        case _:
                                            input('Opção inválida. Pressione qualquer tecla para continuar.')
                                            continue
                    if logou == False:
                        input('Login inválido. Pressione qualquer tecla para continuar.')
                        limpaTela()
                        continue   
            case 3:
                rodando = True
                while rodando:
                    usuario = input('Usuário (ou sair): ')
                    if usuario == 'sair':
                        break
                    senha = input('Senha: ')
                    logou = False
                    for gerente in fc.gerente:
                        if gerente['nome'] == usuario and gerente['senha'] == senha:
                            input(f'Olá {usuario}. Login realizado com sucesso.\n')
                            logou = True
                    limpaTela()
                    print('Menu Gerente')
                    print('[1] Atualizar produto')
                    print('[2] Listar funcionários')
                    print('[3] Relatórios')
                    print('[4] Voltar')
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
                                fc.atualizar_funcionarios(fc.funcionarios)
                            case 3:
                                limpaTela()
                                produto.menu_relatorios()
                            case 4:
                                break
                            case _:
                                input('Opção inválida. Pressione qualquer tecla para continuar.')
                                continue
            case 4:
                input('Saindo...')
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



