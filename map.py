'''
Map
Data: 23/01/2022


'''
# Utilizado para importar dados de outros scripts
from MapData import pessoas, produtos, lista

print(pessoas)
print(produtos)

# Map ----
# Utilizado para transformar algum objeto
# Dentro do map utilizamos uma função para ser implementada
# dentro de cada valor desse objeto (i]terável)

nova_lista = map(lambda x: x * 2, lista)
print(nova_lista) # No entanto, ela retorna um iterador
print(list(nova_lista)) # Agora temos uma lista novamente

# No entanto, muitas vezes não vai ser útil para listas,
# mas sim para funções mais complexas

# Por exemplo, no problema anterior
nova_lista = [x * 2 for x in lista]
print(nova_lista) # Resultado é o mesmo

# Map para preços aumentando o preço em 5%
precos = map(lambda p: p['preço'] * 1.05, produtos)
print(list(precos))

# Utilizar para aumentar o preço dentro da lista
def aumento_preco(p):
    p['preço'] = round(p['preço'] * 1.05, 2)
    return p

novos_produtos = map(lambda p: aumento_preco(p), produtos)
print(list(novos_produtos))

