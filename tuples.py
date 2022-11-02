"""
Tuples
Data: 27/12/2021

Tuples não podem ser alteradas. Essa é a principal
diferença entre uma tuple e uma lista
"""
# Classe tuple
tupla = ()
# Para adicionar elementos em uma tupla é necessário fazer
# na criação dessa
tupla_numerica = (1, 2, 3, 4, 5)
# Podemos criar uma tupla sem parenteses também
tupla_sem_parenteses = 1, 2, 3, 4, 5
# Uma tupla de um elemento sem parenteses deve ser feita
# colocando uma virgula.
tupla_singular = 1,
# Junção de tuplas
print(tupla_sem_parenteses + tupla_singular)
# Desempacotar tuplas funciona da mesma forma que para listas
# Multiplicador de uma tupla também é possível
print(tupla_sem_parenteses * 2)
# É possível converter tuplas em listas
lista_numerica = list(tupla_numerica)
# A lista pode ser modificada

