"""
Static Method
Data: 24/01/2022

Para static methods não precisamos nem da instância, nem da classe
"""

from datetime import datetime
from random import randint


class BasePessoa:
    ano_atual = int(datetime.strftime(datetime.now(), "%Y"))

    def __init__(self, nome, idade):
        self.ano_nascimento = None
        self.nome = nome
        self.idade = idade

    # Método de instância
    def alterar_idade(self, idade):
        if idade == self.idade:
            print("A nova idade é igual a anterior.")
        else:
            self.idade = idade
            print("Idade alterada.")

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod # Não necessita nem da classe, nem da instância
    def gera_id():
        rand_id = randint(10000, 19999)
        #  Temos que criar variáveis não relacionadas a classe/instância
        return rand_id

