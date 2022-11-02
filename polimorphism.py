"""
Polimorphism
26/01/2022

Polimorfirmo é o príncipio que permite que classes derivadas de uma mesma superclasse tenham métodos iguais
(de mesma assinatura), mas comportamentos diferentes.
Mesma assinatura = Mesma quantidade e tipo de paramêtros
Já utilizamos isso
"""
from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def listar(self, msg):
        pass


class B(A):
    def listar(self, msg): # É necessário a mesma assinatura, tendo em vista que a classe A é abstrata
        print(f"B: {msg}")


class C(A):
    def listar(self, msg):
        print(f"C: {msg}")


# Polimorfirsmo:
b = B()
c = C()
b.listar("Olá!")
c.listar("Oi!")


