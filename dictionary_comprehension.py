'''
Dictionary Comprehension
Data: 06/01/2022

Melhorar o código na perspectiva de número de
linhas e de velocidade
'''

lista = [
    ['Fernando', 22],
    ['Isa', 20],
]

# Cria um dicionário a partir de uma lista ----
dicionario = {x: y for x, y in lista}
print(dicionario)

# Possível também mudar uma das variáveis
dicionario = {x.upper(): y for x, y in lista}
print(dicionario)

# enumerate pode ser útil também
numero_dicionario = {x: y for x, y in enumerate(range(3))}
print(numero_dicionario)

# Trabalhar somente um dado traria um set comprehension
set_nomes = {x for x, y in lista} # necessário especificar se estamos
# tratando do primeiro ou segundo valor
print(set_nomes)

# Exemplo ----
quadrado = {f'Chave {x}': x**2 for x in range(5)}
print(quadrado)