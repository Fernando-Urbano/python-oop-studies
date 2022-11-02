'''
Zip
Data: 06/01/2022

zip - unindo iteráveis
zip_longest - itertools
'''

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Rio de Janeiro']

estados = ['SP', 'MG', 'BA', 'RJ']

# Gera um gerador para juntar as listas
cidades_estados = zip(cidades, estados)

# Formas de ver os valores de cidades_estados:
print(next(cidades_estados))
print(next(cidades_estados))
# Em diante...

# Outra forma de realizar isso é atraves do for:
for valor in cidades_estados:
    print(valor)
# O tipo de objeto é zip
# Também pode ser printado como:
print(list(cidades_estados))

# O zip_longest irá unir todas as variáveis pela maior lista.
# O zip irá unir pela menor lista.
cidades_europa = ['Rome', 'Madrid', 'Paris', 'London']
estados_europa = ['Italy', 'Spain', 'France']

# Para usar o zip_longest, é necessário importar itertools
import itertools
referencia_europa_completo = itertools.zip_longest(
    cidades_europa,
    estados_europa,
    fillvalue='País' # Como preenche o que não tem valor
)
for valor in referencia_europa_completo:
    print(valor)
print("#" * 20)
referencia_europa = zip(cidades_europa, estados_europa)
for valor in referencia_europa:
    print(valor)

# Count ----
# Também é importado pelo itertools
indice_europa = itertools.count()
cidades_europa = ['Rome', 'Madrid', 'Paris', 'London']
estados_europa = ['Italy', 'Spain', 'France']

cidades_estados_europa = zip(
    indice_europa, # Faz com que haja um índice para os valores no zip
    estados_europa,
    cidades_europa
)

for valor in cidades_estados_europa:
    print(valor)

for valor in cidades_estados_europa:
    print(valor)