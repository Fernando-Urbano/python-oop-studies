'''
Iterables, Iterators and Generators
Data: 06/01/2022
'''

import sys
import time

# Iterables ----
# Uma lista é um iterável
# Para confirmar isso, podemos perguntar se
lista = list(range(3))
print(hasattr(lista, '__iter__')) # Resposta será verdadeira
# Se um objeto é iterável, podemos usar o for dentro dele
# Números não são iteráveis
print(hasattr(3, '__iter__')) # Resposta é False

# Iterador ----
# O iterador é conseguido a partir de elementos iteráveis
lista = list(range(10))
print(hasattr(lista, '__next__')) # pergunta se é um iterador

# Para que a resposta seja verdadeira, é necessário:
lista = iter(lista)
# Agora poderei iterar a lista
print(next(lista))
print(next(lista))
print(next(lista))

# Descobrindo quanto de memória determinado objeto consome
print(sys.getsizeof(lista)) # Em bytes
lista = list(range(1000))
print(sys.getsizeof(lista)) # Em bytes

# Os geradores servem para trabalhar com listas grandes de forma
# a trabalhar com um elemento por vez

# Generators ----
def gerar():
    r = []
    for n in range(15):
        r.append(n)
        time.sleep(0.1)
    return r

obj = gerar()

# Para transformar a função em um gerador, utilizo o yield
def gerar():
    r = []
    for n in range(10):
        yield n
        time.sleep(0.1)

obj_ger = gerar()

for value in obj_ger:
    print(value)

# Os geradores são iteráveis. Portanto, podemos usar
obj_ger = gerar()

print('Próximo valor:', next(obj_ger))
print('Próximo valor:', next(obj_ger))
print('Próximo valor:', next(obj_ger))

# Outra forma de criar um gerador:
# Dentro de list comprehension utilizar parenteses ao inves
# de colchetes

lista_geradora = (x for x in range(1000))
print(lista_geradora)