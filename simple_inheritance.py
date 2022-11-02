"""
Simple Inheritance

Associação: Usa
Agregação: Tem
Composição: É dono
Herança: É
"""

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

cliente1 = Cliente('Luiz', 22)

# Se além de cliente, formos ter aluno com uma formatação similar, pode ser vantajoso usar a herança
# Como melhorar o código:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def relacao_empresa(self): # Valido também para as classes que herdam
        print(f'{self.nome} é {self.nomeclasse}')


class Cliente(Pessoa):  # A classe cliente "herda" os atributos da classe pessoa
    def comprar(self):  # Comprar é um atributo especifico da classe aluno
        print(f'{self.nomeclasse} comprando...')


class Aluno(Pessoa):  # A classe aluno "herda" os atributos da classe pessoa
    def estudar(self):  # Estudar é um atributo especifico da classe aluno
        print(f'{self.nomeclasse} estudando...')


# A herança funciona de cima para baixo. Cliente, Aluno são hierarquias
cliente2 = Cliente('Maria', 32)
aluno1 = Aluno('Júlio', 56)

cliente2.relacao_empresa()

# O cliente não pode estudar
try:
    cliente2.estudar()
except AttributeError as error:
    print(error)


# Multiplas Heranças ----
# Podemos ter subclasses ainda mais completas:
class ClienteVip(Cliente):
    def comprar_com_desconto(self):
        print("Comprando com desconto...")