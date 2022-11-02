'''
Reduce
Data: 23/01/2022

'''
# Utilizado para importar dados de outros scripts
from MapData import pessoas, produtos, lista
import functools

soma_lista = functools.reduce(lambda acumulador, i: i + acumulador, lista, 0)
# O "i + acumulador" retorna a ser o acumulador
# Assim, o acumulador muda de valor ao longo da lista
print(soma_lista)

soma_precos = functools.reduce(lambda acumulador, p: p['preço'] + acumulador, produtos, 0)
print(soma_precos)

# Conseguir a idade média das pessoas
soma_idades = functools.reduce(lambda ac, p: ac + p['idade'], pessoas, 0)
print(f'Idade média da lista de pessoas: {round(soma_idades / len(pessoas), 2)}')

