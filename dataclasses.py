"""
Dataclasses
Data: 06/02/2022

O módulo dataclasses fornece um decorador e funções para criar automaticamente métodos, como __init__(), __repr__(),
__eq__(), etc. em classes definidas pelo usuário
Basicamente, dataclasses são syntax sugar para criar classes normais.
Foi originalmente descrito na PEP 557 e adicionado na versão 3.7 do Python
Ela gera código automaticamente (code generator)
"""
from dataclasses import dataclass, asdict


@dataclass
class Pessoa:
    nome: str
    sobrenome: str


# A classe já vem com alguns métodos, como init, repr, etc;


p1 = Pessoa('Fernando', 'Rocha')
print(p1.nome)
print(p1)

# No dataclasses podemos desativar alguns métodos.
# Além disso, é possível fazer um __post_init__() que irá ser executado após o init:

@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'

# Atenção, o método eq também já é escrito
p1 = Pessoa('Joana', 'Cota')
p2 = Pessoa('Joana', 'Cota')
print(p1 == p2)


# Para não fazer determinado método
@dataclass(eq=False, repr=False, order=False, frozen=False, init=True)
# Frozen: não permite editar a classe (classe se torna imutável)
# Order: serve para entender qual a ordem na hora de fazer o sort.
# Se order estiver como true, os métodos sort/sorted funcionam
class Pessoa:
    nome: str
    sobrenome: str

    def __post_init__(self):
        if not isinstance(self.nome, str):
            raise TypeError(
                f'Invalid type {type(self.nome).__name__} != str em self {self}'
            )

    @property
    def nome_completo(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'


# Transformar classe em dicionário

p1 = Pessoa('Joana', 'Cota')
print(asdict(p1))

