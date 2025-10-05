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
import produto
import clientes
import vendas


# Vai ter um menu que seleciona gerente ou cliente e sair
while True:
    try:
        limpaTela()
        opcao = int(input('Digite [1] se você é Cliente\nDigite [2] se você é Gerente\n[3] Sair.\n'))
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
                                produto.listar_produtos()
                            case 3:
                                print('Voltar')
                                continue
                            case _: 
                                input('Opção inválida. Pressione qualquer tecla para continuar.')
                                continue
            case 2:
                while True:
                    limpaTela()
                    print('Menu Gerente')
                    print('[1] Adicionar produto')
                    print('[2] Remover produto')
                    print('[3] Atualizar produto')
                    print('[4] Listar produtos')
                    print('[5] Listar clientes')
                    print('[6] Relatórios')
                    print('[7] Voltar')
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
                                print('Listar produtos')
                                produto.listar_produtos()
                            case 5:
                                limpaTela()
                                print('Listar clientes')
                                produto.listar_clientes()
                            case 6:
                                limpaTela()
                                print('Relatórios')
                                produto.menu_relatorios()
                            case 7:
                                break
                            case _: 
                                input('Opção inválida. Pressione qualquer tecla para continuar.')
                                continue 
                    
            case 3:
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



