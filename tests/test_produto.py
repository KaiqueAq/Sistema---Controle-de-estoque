import unittest
import sys
import os

# Adicionar o diretório raiz ao path para importar módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import produto
import clientes

class TestProduto(unittest.TestCase):

    def setUp(self):
        """Configura o ambiente de teste"""
        # Carregar dados de teste
        clientes.load_dados()
        # Limpar produtos para teste
        clientes.dados['produtos'] = []

    def test_gerar_codigo_produto_vazio(self):
        """Testa geração de código quando não há produtos"""
        codigo = produto.gerar_codigo()
        self.assertEqual(codigo, 1)

    def test_gerar_codigo_com_produtos(self):
        """Testa geração de código quando há produtos"""
        clientes.dados['produtos'] = [
            {'codigo': 1, 'nome': 'teste1'},
            {'codigo': 3, 'nome': 'teste2'}
        ]
        codigo = produto.gerar_codigo()
        self.assertEqual(codigo, 4)

    def tearDown(self):
        """Limpa após os testes"""
        clientes.dados['produtos'] = []

if __name__ == '__main__':
    unittest.main()
