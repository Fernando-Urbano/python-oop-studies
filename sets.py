"""
Sets
Data: 06/01/2022

Sets somente aceitam elementos únicos e não contem ordem
dos elementos
"""

primeiro_set = {1, 2, 3, 1, 2, 3}
print(primeiro_set)

# Para criar um set vázio é necessário usar a função set
# Caso contrário, será criado um dicionário
set_vazio = set()
dicionario_vazio = {}
print(type(dicionario_vazio))

primeiro_set.update([1, 2, 3, 4, 5])
# Os números 1, 2 e 3 já existem no set anterior

# União ----
set_n1 = {1, 2, 3, 4, 5}
set_n2 = {1, 2, 5, 6, 7}
print(set_n2.union(set_n1))
print(set_n2 | set_n1)

# Diferença ----
# Somente elementos do set da esquerda
print(set_n1 - set_n2)
# Somente elementos no set da direita
print(set_n2 - set_n1)
# Elementos que não estão nos dois sets
print(set_n2 ^ set_n1)

# Lembrando: a ordem no set não importa

