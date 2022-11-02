"""
Split, Join e Enumerate
Data: 26/12/2021

Split - Divide uma string
Join - Junta uma lista
Enumerate - Enumera elementos de uma lista
"""
# Split ----
frase = 'Meu nome é Fernando, tenho 22 anos.'
lista = frase.split(' ')
print(lista)
sentencas = frase.split(',')
print(sentencas)

# Join ----
# Junta todos os elementos de uma lista pelo
# carácter utilizado. No caso "-".
juncao = '-'.join(lista)
print(juncao)

# Enumerate ----
# Uma forma de definir o índice para cada valor
# de uma lista.
for index, value in enumerate(lista):
    print(index, value)

# Lista dentro de listas ----
lista = [
    ['Fernando', 'Urbano'],
    ['Joana', 'Rocha'],
    ['Ana Luísa', 'Urbano']
]

# Quando realizarmos enumerate com lista em lista,
# o resultado são os valores dentro de cada "sublista".
# O que estamos fazendo é "desempacotar".
for nome, sobrenome in lista:
    print(nome, sobrenome)




