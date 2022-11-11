"""
Class Aggregation.

Data: 25/01/2022
Relação entre classes:
— Agregação: é um tipo de associação. Uma classe usa a outra classe como parte
de si e a outra classe precisa dessa classe. As rodas existem sem os carros e
os carros existem sem as rodas, mas os carros não funcionam de maneira adequada
 sem as rodas.
"""
import functools
import itertools
import re


class CarrinhoDeCompras:
    """Carrinho de Compras."""

    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        produtos_zip = zip(itertools.count(), self.produtos)
        for number, produto in list(produtos_zip):
            print(
                f'{number + 1}) {produto.nome} - '
                + 'R$ {:.2f}'.format(produto.valor)
            )
            # Percebemos que o produto está considerando atributos nome e valor
            # No entanto, isso não foi passado. Surge aí a dependência

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return "Valor a pagar: R$ " + "{:.2f}".format(total)
        # A classe carrinho não precisa de produto para existir,
        # mas ela não faz sentido sem a classe produto

class Produto:
    def __init__(self, nome, valor):
        assert bool(re.search("R[$]", str(valor))) is False, "R$ é não valido."
        assert isinstance(valor, str) == False, "Preço precisa ser um número."
        assert valor > 0, "Preço do produto precisa ser positivo."
        self.nome = nome
        self.valor = valor


carrinho = CarrinhoDeCompras()


# prod1 = Produto('Camiseta', 50)
# carrinho.inserir_produto(prod1)
# carrinho.inserir_produto(prod1)
# prod2 = Produto('Pelucia', 90)
# carrinho.inserir_produto(prod2)
# prod3 = Produto('Raquete', 180)
# carrinho.inserir_produto(prod3)

carrinho.lista_produtos()
carrinho.soma_total()
# Agregação é isso! As classes podem existir, mas uma depende da outra
