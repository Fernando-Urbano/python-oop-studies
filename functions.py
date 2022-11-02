"""
Function
Data: 26/12/2021
"""
def send_hello():
    print("Hello")

print(send_hello())

def squared(n):
    return n ** 2

print(squared)
# Todos os argumentos que sucedem um argumento que possui
# um default também devem possuir um default
def product (n1, n2, n3, n4 = 1, n5 = 1):
    return n1 * n2 * n3 * n4 * n5
# É necessário nomear todos os argumentos que possuem
# default quando utilizamos a nomeação para algum
# argumento que possui default
print(product(1, 2, 3, 4, 1))
print(product(1, 2, 3, n4 = 4, n5 = 1))

# *args e **kwargs ----
# "args" serve para fazer um empacotamento e desempacotamento
def testing(*args):
    print(args)

lista = [1, 2, 3, 4, 5]
# Se fizermos a *lista, a função com args irá desempacotar a lista
print(*lista, sep = "-")
# Se ele não fizer o desempacotamento, ele retornará uma tuple dentro
# de outra tuple.

# "args" funciona como uma tuple. Uma tuple não pode ser alterada
# Um objeto "args" pode ser convertido em lista para que possa
# ser alterado.
def alter_value(*args):
    args = list(args)
    args[0] = args[0] * 4
    return args

print(alter_value(*lista))

# "args" pode funcionar para mais de uma lista
uchoa = ['Edite', 'Leonel']
urbano = ['Fernando', 'Joana']

# Retorna uma única tuple
testing(*uchoa, *urbano)

# *kwargs ----
# Por convenção, chamamos de kwargs
# por serem argumentos de keywords.
# Por exemplo, o argumento nome
def testing(*args, **kwargs):
    print(*args)
    print(*kwargs['nome'], sep='')

testing(*uchoa, *urbano, nome = "Caio")

# Outra forma de acessar o kwargs
def testing(*args, **kwargs):
    print(*args)
    nome = kwargs.get("nome")
    idade = kwargs.get("idade")

    # Forma alternativa de fazer. Possibilita reconhecer
    # se o argumento foi ou não passado.

    if nome:
        print(nome)
    else:
        print("Nome não existe.")

    if idade:
        print(idade)
    else:
        print("Idade não existe.")

# Possibilita que não haja erro
testing(*uchoa, *urbano, nome = "Caio")








