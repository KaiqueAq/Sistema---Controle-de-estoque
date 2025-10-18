# Sistema de Controle de Estoque - Supermercado

Um sistema completo de gerenciamento de estoque para supermercados, desenvolvido em Python. Permite o controle de produtos, clientes, vendas e geração de relatórios para otimizar a gestão do negócio.

## 📋 Descrição

Este projeto implementa um sistema de controle de estoque com funcionalidades avançadas para previsão de vendas e gerenciamento de inventário. O sistema suporta três tipos de usuários: clientes, funcionários e gerentes, cada um com permissões específicas.

## ✨ Funcionalidades

### 👥 Cliente
- **Comprar Produtos**: Navegue pelo catálogo e realize compras
- **Visualizar Catálogo**: Veja produtos disponíveis com preços e estoques

### 👷 Funcionário
- **Gerenciar Produtos**: Adicionar, listar e remover produtos
- **Visualizar Clientes**: Acessar lista de clientes cadastrados
- **Controle de Estoque**: Manter inventário atualizado

### 👔 Gerente
- **Atualizar Produtos**: Modificar preços, custos, estoques e vendas diárias
- **Gerenciar Funcionários**: Listar e atualizar informações de funcionários
- **Relatórios Avançados**:
  - Produtos mais vendidos
  - Previsão de falta de estoque
- **Controle de Contas**: Gerenciar acessos e permissões

### 📊 Sistema Geral
- **CRUD Completo**: Produtos, clientes e vendas
- **Atualização Automática**: Estoque atualizado após cada venda
- **Cálculo de Lucro**: Margem de lucro por produto
- **Previsão de Vendas**: Análise de vendas diárias
- **Persistência de Dados**: Salvamento automático em JSON

## 🏗️ Estrutura do Projeto

```
Sistema---Controle-de-estoque/
├── main.py                 # Arquivo principal do sistema
├── clientes.py             # Módulo de gerenciamento de clientes
├── produto.py              # Módulo de gerenciamento de produtos
├── vendas.py               # Módulo de vendas e relatórios
├── funcionarios.py         # Módulo de funcionários
├── gerente.py              # Módulo de gerente
├── limparTela.py           # Utilitário para limpeza de tela
├── dados.json              # Arquivo de persistência de dados
├── README.md               # Documentação do projeto
└── .gitignore              # Arquivos ignorados pelo Git
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**: Linguagem principal
- **JSON**: Persistência de dados
- **OS**: Interação com sistema operacional
- **Datetime**: Manipulação de datas

## 🚀 Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/sistema-controle-estoque.git
   cd sistema-controle-estoque
   ```

2. **Verifique a instalação do Python**:
   ```bash
   python --version
   ```

## ▶️ Como Executar

1. **Execute o sistema**:
   ```bash
   python main.py
   ```

2. **Selecione o tipo de usuário**:
   - Cliente
   - Funcionário (login necessário)
   - Gerente (login necessário)

## 📖 Como Usar

### Primeiro Acesso
- **Funcionário**: Use as credenciais padrão ou crie novas contas
- **Gerente**: Use as credenciais padrão ou crie novas contas
- **Cliente**: Acesso direto sem login

### Fluxo Básico
1. **Funcionário** adiciona produtos ao sistema
2. **Cliente** realiza compras
3. **Gerente** analisa relatórios e toma decisões

## 📊 Relatórios Disponíveis

- **Produtos Mais Vendidos**: Ranking por volume de vendas diárias
- **Previsão de Falta**: Produtos com risco de esgotamento
- **Análise de Lucro**: Margem de lucro por produto

## 🔧 Configuração

O sistema utiliza um arquivo `dados.json` para persistência. Os dados iniciais incluem:
- 5 produtos padrão
- 9 clientes pré-cadastrados
- Lista vazia de vendas

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Desenvolvedores

- **Kaique**: Desenvolvedor principal

## 📞 Suporte

Para dúvidas ou sugestões, entre em contato através das issues do GitHub.

---

**Nota**: Este sistema foi desenvolvido como projeto acadêmico para demonstrar conceitos de programação orientada a objetos, manipulação de dados e interface de usuário em console.
