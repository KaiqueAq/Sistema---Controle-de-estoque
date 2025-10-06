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
                    print('[1] Cadastrar')
                    print('[2] Comprar')
                    print('[3] Voltar')
                    try:
                        opcao = int(input('Digite a opção desejada: '))
                    except ValueError:
                        input('Opção inválida. Pressione qualquer tecla para continuar.')
                        continue
                    else:
                        match opcao:
                            case 1:
                                print('Menu Cadastro')
                                clientes.cadastrar_cliente()
                            case 2:
                                print('Menu Compra') 
                                clientes.comprarProduto()
                            case 3:
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
                                print('[1] Cadastrar cliente')
                                print('[2] Atualizar cliente')
                                print('[3] Sair')
                                try:
                                    opcao = int(input('Digite a opção desejada: '))
                                except ValueError:
                                    input('Digite uma opção válida.')
                                    continue
                                else:
                                    match opcao:
                                        case 1:
                                            clientes.cadastrar_cliente()
                                        case 2: 
                                            pass
                                        case 3: rodando = False; break
                    if logou == False:
                        input('Login inválido. Pressione qualquer tecla para continuar.')
                        limpaTela()
                        continue   
            case 3:
                while True:
                    limpaTela()
                    print('Menu Gerente')
                    print('[1] Adicionar produto')
                    print('[2] Remover produto')
                    print('[3] Atualizar produto')
                    print('[4] Listar produtos')
                    print('[5] Listar clientes')
                    print('[6] Listar funcionários')
                    print('[7] Relatórios')
                    print('[8] Voltar')
                    try:
                        opcao = int(input('Digite a opção desejada: '))
                    except ValueError:
                        input('Digite uma opção válida.')
                        continue
                    else:
                        match opcao:
                            case 1:
                                limpaTela()
                                print('Adicionado produto...')
                                produto.adicionar_produto()
                            case 2:
                                limpaTela()
                                print('Removendo produto...')
                                produto.remover_produto()
                            case 3:
                                limpaTela()
                                print('Atualizando produto...')
                                produto.atualizar_produto()
                            case 4:
                                limpaTela()
                                print('Listando produtos...')
                                produto.listar_produtos()
                            case 5:
                                limpaTela()
                                print('Listando clientes...')
                                clientes.listar_clientes(clientes.clientes)
                            case 6:
                                limpaTela()
                                print('Listando funcionários...')
                                fc.atualizar_funcionarios(fc.funcionarios)
                            case 7:
                                limpaTela()
                                print('Relatórios')
                                produto.menu_relatorios()
                            case 8:
                                break
                            case _: 
                                input('Opção inválida. Pressione qualquer tecla para continuar.')
                                continue 
                    
            case 4:
                print('Saindo...')
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



