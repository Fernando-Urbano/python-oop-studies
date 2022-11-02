'''
Combinations, Permutations and Products
Data: 23/01/2022

Combinação: ordem não importa
Permutação: ordem importa
Ambos não repetem valores únicos
Produto: ordem importa e repete valores únicos
'''
import itertools

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia']
# Para saber combinações

number = 0
for grupo in itertools.combinations(pessoas, 2):
    print(grupo) # Ordem importa
    number += 1

print(f'Número de combinações: {int(number)}')
print("#" * 20)

number = 0
for grupo in itertools.permutations(pessoas, 2):
    print(grupo) # Ordem importa
    number += 1

print(f'Número de combinações: {int(number)}')
print("#" * 20)

number = 0
for grupo in itertools.product(pessoas, repeat=2):
    print(grupo)  # Ordem importa e possos valores repetidos
    number += 1
print(f'Número de combinações: {int(number)}')