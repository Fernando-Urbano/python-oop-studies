"""
Metaclass
Data: 01/02/2022

São classes que criam outras classes
"""


class A:
    attr = 'Valor'
    # Os objetos que crio a partir dessa classe terão esse atributo


a = A()
b = A()
c = A()


# a, b, c serão instâncias da classe
# Em python, tudo é um objeto, inclusive as classes
# Portanto, existe uma classe que cria um objeto de tipo classe


# Pensando no problema ----
class A:
    def falar(self):
        self.escutar()


class B(A):
    pass

# No caso, quando fazemos um programa desse tipo em que a classe B
# deveria definir escutar, mas não definiu, como podemos fazer para que o problema seja atribuido
# a parte do código que esqueceu de fazer a parte "escutar" da classe B?


# Criar uma meta classe
class Meta(type):
    def __new__(mcs, name, basis, namespace):
        return type.__new__(mcs, name, basis, namespace)
        # O __new__ mostra quando uma nova classe é criada
        # name: nome da classe
        # namespace: atributos e métodos criados naquela classe


# Agora iremos herdar A da classe meta de forma que A irá se comportar da mesma forma dessa meta classe
class A(metaclass=Meta):
    def falar(self):
        self.escutar()


# Para colocar que o problema é referente a classe B:
class Meta(type):
    def __new__(mcs, name, basis, namespace):
        if name == 'A':
            return type.__new__(mcs, name, basis, namespace)

        if 'escutar' not in namespace:
            print(f'Método "escutar" precisa ser criado {name}.')
        else:
            if not callable(namespace['escutar']):
                print(f'Método "escutar" precisa ser um método, não um atributo {name}.')
                # Se não, podemos criar um atributo que ele não irá gerar esse problema

        print(namespace)

        return type.__new__(mcs, name, basis, namespace)

class A(metaclass=Meta):
    def falar(self):
        self.escutar()


class B(A):
    testar = 'Valor'
    pass

teste = B()
teste.falar()



