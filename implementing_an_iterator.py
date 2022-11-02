"""
Implement an Iterator
Data: 06/02/2022

Vamos recriar a lista do python.
Entender como é aplicada
"""


class MinhaLista:
    def __init__(self):
        self.__items = []
        self.__index = 0
        # "__" serve para dizer que é bloqueado

    def add(self, valor):
        self.__items.append(valor)

    # Implementando o protocolo do iterator
    def __iter__(self):
        return self
        # No caso, estamos falando que o padrão dessa classe é a própria classe

    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration  # Irá parar quando a lista terminar
        # Ele irá retornar a próximo elemento da minha lista

    # Para que a classe seja um iterator, é necessário que tenhamos um
    # iter definido e um next

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__items})'


lista = MinhaLista()
lista.add('Edite')
lista.add('Matheus')

print(lista)

for nome in lista:
    print(nome)


# No entanto, ele ainda não conseguirá indexar. Ele não é subscribable.
# É necessário colocar o método __getitem__
class MinhaLista:
    def __init__(self):
        self.__items = []
        self.__index = 0
        # "__" serve para dizer que é bloqueado

    def add(self, valor):
        self.__items.append(valor)

    # Implementando o protocolo do iterator
    def __iter__(self):
        return self
        # No caso, estamos falando que o padrão dessa classe é a própria classe

    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration  # Irá parar quando a lista terminar
        # Ele irá retornar a próximo elemento da minha lista

    # Para que a classe seja um iterator, é necessário que tenhamos um
    # iter definido e um next

    def __getitem__(self, item):
        return self.__items[item]

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__items})'


lista = MinhaLista()
lista.add('Bia')
print(lista[0])

# No entanto, ainda não é possível alterar um “item”
try:
    lista[0] = 'João'
except TypeError as error:
    print(error)


class MinhaLista:
    def __init__(self):
        self.__items = []
        self.__index = 0
        # "__" serve para dizer que é bloqueado

    def add(self, valor):
        self.__items.append(valor)

    # Implementando o protocolo do iterator
    def __iter__(self):
        return self
        # No caso, estamos falando que o padrão dessa classe é a própria classe

    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration  # Irá parar quando a lista terminar
        # Ele irá retornar a próximo elemento da minha lista

    # Para que a classe seja um iterator, é necessário que tenhamos um
    # iter definido e um next

    def __getitem__(self, item):
        return self.__items[item]

    def __setitem__(self, key, value):
        if key >= len(self.__items):
            self.__items.append(value)
        else:
            self.__items[key] = value

    def __delitem__(self, key):
        del self.__items[key]

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__items})'


print("\n" * 3)
lista = MinhaLista()
lista.add('Bia')
print(lista[0])
lista[0] = 'João'
print(lista[0])
