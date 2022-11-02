"""
Overloading Operators
Data: 01/02/2022

Comportamento dos operadores é definido por métodos especiais.
Vamos alterar o comportamento de operadores com classes definidas pelo usuário.
O operador é, por exemplo, "+", "-", etc...
Quando eu crio uma classe, esses operadores não são definidos. Os métodos servem para definí-los
"""


class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


r1 = Retangulo(2, 5)
r2 = Retangulo(4, 10)

try:
    print(r1 + r2)  # O python não saberá o que fazer entre os dois objetos
except TypeError as error:
    print(error)

# O Python tem diversos métodos especiais que podem servir para definir isso
# Os métodos especiais são aqueles que possum "__" no início e no fim


class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # "other" é o segundo objeto
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Retangulo(new_x, new_y)
        # Estamos ensinando o enterpretador do python a entender "+" para a classe
        # No caso, ele está retornando um outro objeto da mesma classe

    def __repr__(self):  # Método de como a classe é representada
        return f"<class 'Retangulo({self.x}, {self.y})'>"
        # Forma como iremo mostrar a classe

r1 = Retangulo(2, 5)
r2 = Retangulo(4, 10)

print(r1 + r2)  # Irá me dar um novo Retangulo


# Temos diversos outros métodos especiais, por exemplo, para maior, menor, etc...
# Adicionando maior que:


class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # "other" é o segundo objeto
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Retangulo(new_x, new_y)
        # Estamos ensinando o enterpretador do python a entender "+" para a classe
        # No caso, ele está retornando um outro objeto da mesma classe

    def __repr__(self):  # Método de como a classe é representada
        return f"<class 'Retangulo({self.x}, {self.y})'>"
        # Forma como iremo mostrar a classe

    def get_area(self):
        return self.x * self.y

    def __le__(self, other):  # Checa se o primeiro é less o segundo
        self.area = self.get_area()
        other.area = other.get_area()

        if self.area < other.area:
            return True
        else:
            return False

    def __gt__(self, other):  # Checa se o primeiro é greater than o segundo
        self.area = self.get_area()
        other.area = other.get_area()

        if self.area > other.area:
            return True
        else:
            return False

    def __eq__(self, other):  # Checa se o primeiro é equal ao segundo
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


r1 = Retangulo(2, 5)
r2 = Retangulo(4, 10)

print(r1 > r2)
print(r1 < r2)

r3 = Retangulo(2, 5)
print(r2 == r3)
print(r1 == r3)




