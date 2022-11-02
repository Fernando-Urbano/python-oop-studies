'''
List Comprehension
Data: 06/01/2022

Melhorar o código na perspectiva de número de
linhas e de velocidade
'''


lista_base = [1, 2, 3, 4, 10]
lista_derivada = [variavel for variavel in lista_base]

# Printando a mesma lista que a lista base
print(lista_derivada)

# Utilização de uma mudança na lista base
lista_derivada = [variavel * 2 for variavel in lista_base]

# Printando a mesma lista que a lista base
print(lista_derivada)

# Realizar listas dentro de lista
lista_derivada = [(v1, v2) for v1 in lista_base for v2 in range(3)]
print(lista_derivada)
# Funciona de forma similar a um expand.grid no R

# Realizar mudanças em uma lista ----
lista_nomes = ['fernando', 'rocha', 'urbano']
lista_maiuscula = [nome.upper() for nome in lista_nomes]
print(lista_maiuscula)

# Exemplo com tupla ----
tupla = (
    ('Fernando', 22),
    ('Isa', 20),
    ('Bruno', 18)
)
# Inverter a ordem
tupla_invertida = [(idade, nome) for (nome, idade) in tupla]
print(tupla_invertida)

# Exemplo
lista_numero = list(range(100))
lista_div3 = [n for n in lista_numero if n % 3 == 0]
print(lista_div3)
# Cria nova lista somente com números que são divisíveis por 3
# Lista de números divisíveis por 3 e por 8
lista_div3_div8 = [n for n in lista_numero if n % 3 == 0 and n % 8 == 0]
print(lista_div3_div8)

# Utilizando com o else
lista_ndiv = [n if n % 3 == 0 and n % 8 == 0 else 0 for n in lista_numero]
print(lista_ndiv)