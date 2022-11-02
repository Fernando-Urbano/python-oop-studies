"""
Abstract Classes
26/01/2022

A ideia do exercício em que todas as pessoas eram possíveis clientes
ou possíveis alunos parte da ideia de que Pessoa é uma classe abstrata.
Naquela aula, podemos instânciar a classe Pessoa, no entanto, pode ser interessante
não dar a possibilidade de a classe ser instanciada.
Um método abstrato: o método não tem corpo, mas que obriga que as classes filhas desenvolvam
esse método
"""
from abc import ABC, abstractmethod


# abc significa abstract base class
# Fazendo a importação do que temos acima, conseguimos já fazer classes abstratas
class A(ABC):  # ABC é uma classe. Classe A herda da classe ABC
    pass


# Dessa forma, a classe ainda pode ser instanciada:
a1 = A


# Para que a classe não possa ser instanciada, é necessário que coloquemos um método abstrato
class A(ABC):
    @abstractmethod
    def listar(self):
        print('Listado')


try:
    a1.listar()  # Isso é instanciar um objeto de uma classe
except AttributeError as error:
    print(error)


# Dessa forma, não podemos instanciar uma classe que herda A sem que definamos o método que está como
# abstrato

class B(A):
    pass


try:
    b1 = B()
    b1.listar()
except TypeError as error:  # O problema acontece porque não definimos listar dentro de B
    print(error)


class B(A):
    def listar(self):
        print('Listado')


b1 = B()
b1.listar()


# Exemplo ----
# Estamos fazendo um sistema bancário. Criamos a ideia de Conta, mas ela não pode ser instanciada
# No caso de um novo código, é necessário importar o abc
class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    # Criando os properties
    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    # Criando setter caso nós queiramos mudar o saldo
    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):  # Estamos chegando se valor é uma isntancia de integer ou float
            raise ValueError('Saldo precisa ser númerico')

        self._saldo = valor

    def detalhes(self):
        print(f'Agência: {self.agencia}', end='; ')
        print(f'Conta: {self.conta}', end='; ')
        print(f'Saldo: {self.saldo}')

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo precisa ser númerico')

        self._saldo += valor
        self.detalhes()

    @abstractmethod
    def sacar(self, valor):
        pass  # Iremos definir que o método sacar será implementado em outras classes filhas
        # Assim, forçamos


# Criamos Conta Poupança agora:
class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente.')
            return

        self.saldo -= valor
        self.detalhes()

print("\nConta Poupança:")
cp1 = ContaPoupanca(12412, 412, 0)
cp1.depositar(5)
cp1.depositar(5)
cp1.sacar(7)


# Criando Conta Corrente: temos um limite de saque
class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if (self.saldo + self._limite) < valor:
            print('Saldo insuficiente.')
            return

        self.saldo -= valor
        self.detalhes()


print("\nConta Corrente:")
cc1 = ContaCorrente(12412, 412, 0)
cc1.depositar(5)
cc1.depositar(5)
cc1.sacar(70)
cc1.sacar(45)
