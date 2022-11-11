"""
Script para Importar Classe Carrinho.

Classe carrinhos e produtos são importada usando import
"""
import os
import sys
# os.chdir("/Users/bi003761/Desktop/challenge_asq")

import class_aggregation

carrinho_rian = class_aggregation.CarrinhoDeCompras()

# Produtos no Supermercado ----
maca = class_aggregation.Produto("Maça", 4)
banana = class_aggregation.Produto("Banana", 3.5)
assert type(banana) == class_aggregation.Produto, "Banana não é um produto."
pera = class_aggregation.Produto("Pera", 6)
carne = class_aggregation.Produto("Carne", 12)

# Valor a Pagar ----
print(carrinho_rian.soma_total())

# Produtos comprados por Rian ----
carrinho_rian.inserir_produto(maca)
assert len(carrinho_rian.produtos) > 0, \
    "Carrinho vazio mesmo após adição de produtos."
carrinho_rian.inserir_produto(maca)
carrinho_rian.inserir_produto(banana)
carrinho_rian.inserir_produto(carne)

# Lista de Compras ----
print(carrinho_rian.lista_produtos())

# Valor a Pagar ----
print(carrinho_rian.soma_total())
