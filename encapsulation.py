"""
Encapsulation
Data: 25/01/2022

Na programação orientada a objetos classica,
temos métodos e atributos que são:
— Public: podem ser acessados dentro e fora da classe
— Protected: podem ser acessados dentro da classe ou das filhas daquela classe
— Private: atributo/método somente disponível dentro da classe

Em uma linguagem

"""


class DataBase:
    def __init__(self):
        self.data = {}

    def insert_client(self, id, name):
        if 'clientes' not in self.data:
            self.data['clientes'] = {id: name}
        else:
            self.data['clientes'].update({id: name})

    def clients_list(self):
        for id, name in self.data['clientes'].items():
            print(f"ID: {id}; Nome: {name}")

    def erase_client(self, id):
        del self.data['clientes'][id]


db = DataBase()
db.insert_client(1, 'Joana')
db.insert_client(2, 'Fernando')
db.insert_client(3, 'Bruno')

print(db.data)
db.clients_list()

# Na classe que temos em cima, o self.data é público.
# Ele é acessível dentro e fora da classe
# Portanto, podemos modificar o self.data por fora da classe
db.data = "Alteração"
try:
    db.clients_list()
except TypeError as error:
    print(error)

try:
    db.insert_client(4, 'Ana Luísa')
except TypeError as error:
    print(error)


# No python, para utilizar, public, private, protected, utilizamos convenções
# "_" antes da varável: recomenda-se que você não acesse esse atributo
# Caso isso for feito, o atributo passa a não ser mais visível. É privado

class DataBase:
    def __init__(self):
        self._data = {}

    def insert_client(self, id, name):
        if 'clientes' not in self._data:
            self._data['clientes'] = {id: name}
        else:
            self._data['clientes'].update({id: name})

    def clients_list(self):
        for id, name in self._data['clientes'].items():
            print(f"ID: {id}; Nome: {name}")

    def erase_client(self, id):
        del self._data['clientes'][id]


# O "__" seria fortemente recomendado que você não pode mudar
# O "protected" realmente proibe que eu acesse a classe

class DataBaseProtected:
    def __init__(self):
        self.__data = {}

    def insert_client(self, id, name):
        if 'clientes' not in self.__data:
            self.__data['clientes'] = {id: name}
        else:
            self.__data['clientes'].update({id: name})

    def clients_list(self):
        for id, name in self.__data['clientes'].items():
            print(f"ID: {id}; Nome: {name}")

    def erase_client(self, id):
        del self.__data['clientes'][id]


db = DataBaseProtected()

db.insert_client(1, 'Joana')
db.insert_client(2, 'Fernando')
db.insert_client(3, 'Bruno')

db.__data = "Alteração"  # Irá criar um outro atributo agora visível
# No entanto, o atributo criado dentro da classe permanece invísível e não pode ser modificado
# Isso mostra que o atributo aqui não é acessável por fora da classe
try:
    db.clients_list()
    print(db.__data)
except TypeError as error:
    print(error)

try:
    db.insert_client(4, 'Ana Luísa')
except TypeError as error:
    print(error)


# E se eu quisesse liberar acesso aos valores do __dados?
# Utilizo getters and setters
class DataBaseProtected:
    def __init__(self):
        self.__data = {}

    @property
    def data(self):
        return self.__data

    # Assim, eu consigo alterar data, mas não consigo alterar __data
    # O python, de qualquer forma, não irá permitir que a gente configure a variável dados dentro da classe
    # temos em vista que não criamos um setter

    def insert_client(self, id, name):
        if 'clientes' not in self.__data:
            self.__data['clientes'] = {id: name}
        else:
            self.__data['clientes'].update({id: name})

    def clients_list(self):
        for id, name in self.__data['clientes'].items():
            print(f"ID: {id}; Nome: {name}")

    def erase_client(self, id):
        del self.__data['clientes'][id]


db = DataBaseProtected()
db.insert_client(1, 'Joana')
db.insert_client(2, 'Fernando')
db.insert_client(3, 'Bruno')

try:
    db.data = 'Outro Valor'
except AttributeError as error:
    print(error)

# Irá levantar uma excessão falando que não posso "setar" esse atributo, tendo em vista que a classe
# não tem um setter para esse atributo
# No entanto, eu posso printar esse atributo
print(db.data)

# Em resumo, "_" busque não tocar
# "__" você não pode tocar
