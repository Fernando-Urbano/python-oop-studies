"""
Script para Importar Classe Carrinho.

Classe carrinhos e produtos são importada usando import
"""
import os
import sys
import pickle

from ../class_aggregation import CarrinhoDeCompras, Produto

carrinho_rian = CarrinhoDeCompras()

# Produtos no Supermercado ----
maca = Produto("Maça", 4)
banana = Produto("Banana", 3.5)
assert type(banana) == Produto, "Banana não é um produto."
pera = Produto("Pera", 6)
carne = Produto("Carne", 12)

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

output = open('carrinho_rian.pkl', 'wb')
pickle.dump(carrinho_rian, output)

