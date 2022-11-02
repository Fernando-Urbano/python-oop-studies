"""
OOP Exercise
Criar um sistema bancário com:
    - cliente;
    - contas;
    - banco.

Devem existir contas:
    - corrente: que possuem limite extra
    - poupança.

Dicas:
Criar classe Cliente que herda da classe Pessoa:
    Pessoa tem nome e idade (com getters)
    Cliente tem conta (Agregação da classe ContaCorrente ou ContaPoupança)
Criar classes ContaPoupanca e ContaPoupanca que herdam de Conta
    ContaCorrente deve ter limite extra
    Contas têm agências, número de conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e Poliformismo - as subclasses que
        irão implementar o método sacar)
Criar classe Banco para agregar classes de clientes e de contas (Agregação)
Banco será responsável por autenticar o cliente e as contas das seguintes maneiras:
    Checar se a agência é daquele banco
    Checar se o cliente é daquele banco
    Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima).
"""


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    # Getter
    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)


class Conta:
    def __init__(self, conta, agencia):
        self._saldo = 0
        self._conta = conta
        self._agencia = agencia

    def depositar(self, valor):
        self._saldo += valor


class ContaCorrente(Conta):
    def __init__(self, conta, agencia, limite):
        super().__init__(conta, agencia)
        self._limite = limite

    def sacar(self, valor):
        if self._saldo - valor > - self._limite:
            self._saldo -= valor
        else:
            print(f'Retirada excede o limite de R$ {self._limite}.')


class ContaPoupanca(Conta):
    def __init__(self, conta, agencia):
        super().__init__(conta, agencia)

    def sacar(self, valor):
        if self._saldo - valor > 0:
            self._saldo -= valor
        else:
            print(f'Retirada o valor em conta.')


class Banco:
    def __init__(self):
        self._contas = {}

    def adicionar_cliente(self, cliente, criacao_conta):
        juncao_conta_cliente = {
            criacao_conta._conta: dict(
                Cliente=dict(Nome=cliente.nome, Idade=cliente.idade),
                Conta=dict(Conta=criacao_conta._conta, Agência=criacao_conta._agencia, Saldo=criacao_conta._saldo)
            )
        }
        self._contas.update(juncao_conta_cliente)

    def mostrar_lista(self):
        for numero_conta, informacoes in self._contas.items():
            print(f'Conta {numero_conta}:')
            for aba, subinfo in informacoes.items():
                for key, value in subinfo.items():
                    print(f'{key}: {value}')
            print('\n')


cl1 = Cliente('Fernando', 22)
cc1 = ContaCorrente(131920, 90, limite=1000)
cl2 = Cliente('Ana', 20)
cc2 = ContaPoupanca(131921, 90)

b1 = Banco()
b1.adicionar_cliente(cl1, cc1)
b1.adicionar_cliente(cl2, cc2)
b1.mostrar_lista()


