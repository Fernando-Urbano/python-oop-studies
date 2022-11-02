'''
Iterables, Iterators and Generators
Data: 06/01/2022
'''

# Exemplos de objetos iteráveis:
# Strings, Lists, Tuples

# Comportamento dos geradores e dos iteradores é diferente
nome = 'Ana Luísa'

for letra in nome:
    print(letra)

print("#" * 20)

# O iterador ele faz o next até o fim
# Outra forma de fazer
nome_iter = iter(nome)
print(next(nome_iter))

# Traz o mesmo resultado que o iterador
try:
    print(next(nome_iter)) # A
    print(next(nome_iter)) # n
    print(next(nome_iter)) # a
    print(next(nome_iter)) #
    print(next(nome_iter)) # L
    print(next(nome_iter)) # u
    print(next(nome_iter)) # í
    print(next(nome_iter)) # s
    print(next(nome_iter)) # a
except:
    pass
