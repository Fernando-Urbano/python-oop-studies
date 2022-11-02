"""
Tipos de Dados
Data: 25/12/2021
"""
print(type("Fernando"))
print("Fernando", type("Fernando")) # Concatena com espaço

# Converter de um tipo para outro ----

print(bool("Fernando"))
int('10')
float('10')
print("Fernando" + "Urbano") # Concatena sem espaço

# Formas de realizar "print" ----

nome = 'Fernando'
idade = 22
print("Nome:", nome + "; Idade:", idade)
print(f'Nome: {nome}; Idade: {idade}')
# Casas decimais para exibir
print(f'Nome: {nome}; Idade: {idade:.2f}')
print(f'Nome: {nome}; Idade: {idade:.1f}')
print('Nome: {}; Idade: {}'.format(nome, idade))
print('Nome: {}; Idade: {}'.format(nome, idade))
# Define qual variável utilizar pela posição no format
# Útil para utilizar a mesma variável mais de uma vez
print('Nome: {0}; Idade: {1}'.format(nome, idade))

# Input - Entrada de Dados ----
nome = input("Nome do Usuário: ")
# Sempre que não definimos a variável, ela é
# uma string quando utilizamos input
idade = int(input("Idade do Usuário: "))

