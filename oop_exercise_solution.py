"""
OOP Exercise Solution

"""
from abc import ABC, abstractmethod


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        # O super serve para fazer a inicialização da classe que herda
        self.conta = None

    def inserir_conta(self, conta):
        self.conta = conta


class Conta(ABC):
    # O ABC é necessário para criar um método abstrato
    def __init__(self, agencia, conta, saldo=0):
        self.conta = conta
        self.agencia = agencia
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(
            f'Agência: {self.agencia}; '
            f'Conta: {self.conta}:\n'
            f'Saldo atualizado: R$ {self.saldo}'
        )

    @abstractmethod
    def sacar(self, valor):
        pass
        # Obriga que o método sacar seja criado


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente.')
            return

        self.saldo -= valor
        self.detalhes()


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=1000):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo + self.limite < valor:
            print('Saldo insuficiente.')
            return

        self.saldo -= valor
        self.detalhes()


class Banco:
    def __init__(self):
        self.agencias = [1, 2, 3, 4, 5]
        self.clientes = []
        self.contas = []

    def inserir_cliente(self, cliente):
        self.clientes.append(cliente)

    def inserir_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return False

        if cliente.conta not in self.contas:
            return False

        if cliente.conta.agencia not in self.agencias:
            return False

        return True


banco = Banco()
c1 = Cliente('Joana', 57)
c2 = Cliente('Bruno', 18)
c3 = Cliente('Bia', 70)

cp1 = ContaPoupanca(agencia=1, conta=200420, saldo=0)
cp2 = ContaPoupanca(agencia=1, conta=200421, saldo=0)
cc3 = ContaCorrente(agencia=1, conta=200422, saldo=0)

c1.inserir_conta(cp1)
c2.inserir_conta(cp2)
c3.inserir_conta(cc3)

c3.conta.sacar(100)

# Com autenticação do banco:
if banco.autenticar(c1):
    c1.conta.sacar(100)
else:
    print('Não foi possível realizar o saque.')

banco.inserir_cliente(c1)
banco.inserir_conta(cp1)

if banco.autenticar(c1):
    c1.conta.sacar(100)
else:
    print('Não foi possível realizar o saque.')

# Polimorfismo: fato do método sacar se comportar de forma diferente na conta corrente a na conta poupança 



