'''
Filter
Data: 23/01/2022


'''
# Utilizado para importar dados de outros scripts
from MapData import pessoas, produtos, lista

nova_lista = filter(lambda x: x > 5, lista)
print(list(nova_lista))

# Utilizando list compreenhension
nova_lista = [x for x in lista if x > 5]
print(list(nova_lista))

# Possível fazer dentro do map também
# Vantajoso porque retorna o
def filtrar_caros(produto, limiar=4):
    produto['caro'] = True if produto['preço'] > limiar else False
    return produto

def_produtos = map(
    lambda x: filtrar_caros(x, limiar=3), produtos
)

print(list(def_produtos))