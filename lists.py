"""
Pass e Ellipsis
Data: 26/12/2021
"""

lista = ['A', 'B', 'C', 'D', 'E']
# Indexar ----
print(lista[1])
print(lista[0::2])

# Adicionar valores na lista ----
lista.append('F')
print(lista)
# Lista é mutável
# Em um lugar especifico
lista = ['A', 'C', 'D', 'E']
lista.insert(1, 'B')
print(lista)

# Remover valores da lista ----
lista.pop() # Retira o último valor
print(lista)
# Refazendo com "del"
del(lista[1:3]) # Removendo o elemento 2 e 3
print(lista)

# Converter objeto iterável em lista
lista = list(range(0, 20, 1))
# Objeto iterável é um objeto que pode ser chamado por index
print(lista[0::2])

# Criar lista vazia
lista_vazia = []