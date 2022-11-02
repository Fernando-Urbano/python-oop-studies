"""
Random
08/02/2022

Módulo random
"""
import random

# Número aleatório inteiro entre determinados valores:
import string

maior_que = 0
menor_que = 0

# Distribuição parece ser uniforme
while maior_que < 1e3 or menor_que < 1e3:
    inteiro = random.randint(0, 3)
    if inteiro >= 2:
        maior_que += 1
    else:
        menor_que += 1

print(maior_que)
print(menor_que)

# Flutuante:
flutuante = random.uniform(1000, 9999)
print(flutuante)

# Número de ponto flutuante entre 0 e 1
print(random.random())

# Número aleatório usando da mesma forma que o range
# Vai gerar um número aleatório pulando de 10 em 10 entre 900 e 999
for i in range(9):
    inteiro = random.randrange(900, 1000, 10)
    print(inteiro)

# Escolher um elemento de uma lista
lista = ['Luiz', 'Fernando', 'Bia', 'Joana', 'Caio', 'Breno']
for i in range(3):
    print(random.choice(lista))

# Escolher fatiamento aleatório
for i in range(3):
    print(random.choices(lista, k=2))  # k representa o número de itens que irá retornar

# Sem poder repetir o mesmo
for i in range(3):
    print(random.sample(lista, k=2))

# Embaralhar a lista original
random.shuffle(lista) # Não retorna nada, mas muda a lista
print(lista)

# Gerar senha aleatória
letras = string.ascii_letters
digitos = string.digits
caracteres = "!@#$%&*"

geral = letras + digitos + caracteres
senha = random.choices(geral, k=20)
# Irá retornar uma senha de 20 caracteres
# Isso na verdade irá gerar uma lista.
# Para gerar uma string, é mais fácil fazer da seguinte forma
senha = ''.join(random.choices(geral, k=20))
print(senha)

# Agora com um número entre 10 e 15 caracteres
for i in range(10):
    senha = ''.join(random.choices(geral, k=random.randint(10, 15)))
    print(senha)





