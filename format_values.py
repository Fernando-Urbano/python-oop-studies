"""
Formatação de Valores
Data: 25/12/2021

:s - formatação de string
:d - formatação de integer
:f - formatação de float

> - Esquerda
< - Direita
^ - Centro
"""
# Formatação de números ----
numero = 1.5
# Quantas casas no total, adicionando antes da virgula
print(f'{numero:0>10}')
print(f'{numero:0>5}')
# Quantas casas no total, adicionando depois da virgula
print(f'{numero:0<5}') # Número de 0s a direita

numero = 3.14159
print(f'{numero:0<2}')

# Formatação de nomes ----
nome = "Fernando Urbano"
(print(f'{nome:#^40}')) # No total, ficam 40 caracteres
# Funciona utilizando o format também
print("{n:#^30} {n:#^30}".format(n=nome))
# Mesmo funciona colocando index
print("{0:#^30} {0:#^30}".format(nome))

# Methods ----
print(nome.ljust(20, "#"))
print(nome.upper()) # Todas maiúsculas
print(nome.title()) # Primeiras maiúsculas
print(nome.lower()) # Todas minúsculas

# Fatiamento de Strings
nome_completo = "Fernando Urbano"
nome = nome_completo[0:8] # Não inclui o último valor
print(nome)
sobrenome = nome_completo[9:] # Com ":" vai até o final
print(sobrenome)
# O index com menos parte do último valor
sobrenome = nome_completo[-6:]
print(sobrenome)

# Do carácter 0 ao 5 saltando de 2 em 2
nome_completo = "Fernando Urbano"
print(nome_completo[0:8:2])

# Saltando de 2 em 2
print(nome_completo[0::2])


