"""
Expressão Condicional com "Or"
Data: 26/12/2021
"""
# Irá realizar com a primeira opção verdadeira que for encontrada
nome = input("Qual o seu nome? ")
print(nome or 'Nome não foi inscrito')
# Caso o nome não for escrito, ele retornará a segunda opção
# O que retorna falso?
a = 0
b = None
c = False
d = []
e = {}

# Não retorna falso:
f = 'Fernando'
g = 22

# Retornar a primeira variável que for verdadeira
variavel_selecionada = a or b or c or d or e or f or g
# Retonará "Fernando", tendo em vista que essa é a primeira variável "True"
print("Variável selecionada: {}".format(variavel_selecionada))