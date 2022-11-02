"""
Class Methods
Data: 24/01/2022

Nos class methods, precisamos da classe e não do objeto
"""
from datetime import datetime


class BasePessoa:
    ano_atual = int(datetime.strftime(datetime.now(), "%Y"))

    def __init__(self, nome, idade):
        self.ano_nascimento = None
        self.nome = nome
        self.idade = idade

    def alterar_idade(self, idade):
        if idade == self.idade:
            print("A nova idade é igual a anterior.")
        else:
            self.idade = idade
            print("Idade alterada.")

# No caso, ano_atual pode ser acessado como atributo, mas não é um atributo do objeto e sim da classe
p1 = BasePessoa(nome='Matheus', idade=23)
print(p1.ano_atual)  # Atributo da classe e não de p1

# Método de Classe ----
# alterar_idade é um método de instância. Um método de classe deve ser decorado com @classmethod
# Ao inves de estarmos nos referindo a instância (self), iremos nos referir a classe:
class BasePessoa:
    ano_atual = int(datetime.strftime(datetime.now(), "%Y"))

    def __init__(self, nome, idade):
        self.ano_nascimento = None
        self.nome = nome
        self.idade = idade

    def alterar_idade(self, idade):
        if idade == self.idade:
            print("A nova idade é igual a anterior.")
        else:
            self.idade = idade
            print("Idade alterada.")

    @classmethod # Ele no caso é também um factor method porque fabrica um objeto
    # Isso funciona como um decorador que está decorando o método abaixo
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
        # O método irá retornar a própria classe, no entanto, baseada nos parametros que temos aqui

p1 = BasePessoa.por_ano_nascimento('Fernando', 1999)
print(p1)
print(p1.nome, p1.ano_nascimento)

# Utilizamos um método de classe quando estamos criando um método relacionado ao molde em geral



