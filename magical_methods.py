"""
Magical Methods
Data: 01/02/2022

Exemplificando alguns métodos mágicos
"""


class A:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)  # Faz com que a classe funcione.
        # Não precisa ser escrito, já é implicito. No caso, o super() é porque todas as classes
        # derivam de object. Se a classe não deriva de nenhuma outra classe criada, ela deriva de
        # object.

    def __init__(self):
        print(
            'Classe iniciada. "__init__" é um método mágico.',
            'Ele não é um construtor, mas na verdade, o construtor é o "__new__".'
        )


a = A()


# Definindo atributos de classe:
class A:
    def __new__(cls, *args, **kwargs):
        cls.name = 'Novo Cliente'  # Isso é um atributo de classe
        # Além disso, podemos definir, métodos, por exemplo

        return super().__new__(cls)

    def __init__(self):
        print('Objeto criado.')


# Padrão de Projeto ----
# No padrão do projeto, somente teremos uma instância do objeto no programa
# Com isso, não será possível criar outra instância.
# Ao tentar instanciar a classe novamente (dizer que um outro objeto é daquela classe),
# isso não será permitido

class A:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_already_exists"):
            cls._already_exists = object.__new__(cls)
            # Faz com que eu não crie

        return cls._already_exists

    def __init__(self):
        print('Objeto criado.')


# Ao fazer isso, qualquer instância que é criada depois da criação da primeira instância,
# é igual a primeira instância criada
b = A()
c = A()
d = A()

print(c == b)
print(c == d)
print(b == d)


# Método __call__ ----
# Faz com que a classe se comporte como uma função
# Dessa forma, é possível chamar a instância da minha classe como uma função
class A:
    def __init__(self):
        print('Objeto criado.')

    def __call__(self, *args, **kwargs):
        print(*args)
        print(**kwargs)


f = A()
f(1, 2, 3, 4, 5, [2, 3, 2, 3])  # Posso chamar a instância como uma função


# Exemplo:
class A:
    def __init__(self):
        print('Objeto criado.')

    def __call__(self, *args, **kwargs):
        resultado = 1

        for i in args:
            resultado *= i

        return resultado


corrida = A()
print(corrida(2, 32, 3, 10, 51))
# A diferença é que podemos utilizar como se fosse uma função

f = A()
f(1, 2, 3, 4, 5, [2, 3, 2, 3])  # Posso chamar a instância como uma função


# __setattr__ ----
# Serve para toda a vez que configurar o atributo novo na minha classe, ele será chamado
class A:
    def __init__(self):
        print('Objeto criado.')


# Tentar fazer isso abaixo irá mudar o nome
print()
g = A()
g.nome = 'Fernando'
try:
    print(g.nome)
except AttributeError as error:
    print('Error')


# Podemos definir se esse atributo pode ou não ser feito
class A:
    def __init__(self):
        print('Objeto criado.')

    def __setattr__(self, key, value):
        if key == 'nome':
            self.__dict__[key] = 'Nome não pode ser alterado'
        else:
            self.__dict__[key] = value


h = A()
h.nome = 'Fernando'
print(h.nome)
h.outro_nome = 'Fernando'
print(h.outro_nome)  # Irá funcionar normalmente


# __del__ ----
# Serve para quando o objeto da classe for deletado pelo python definir o que vai ser feito
# Atenção, nem sempre esse método será chamado. Talvez não seja uma boa ideia colocar ele para
# fazer algo muito importante
class A:
    def __init__(self):
        pass

    def __del__(self):
        print('Objeto deletado.')


# __str__ ----
# Serve para quando printamos um objeto de uma classe
class A:
    def __init__(self):
        pass

    def __str__(self):
        return "<class 'A'>"


j = A()
print(j)


