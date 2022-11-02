"""
Data Structures Stacks and Queues
15/02/2022

Piha (Stack): Lifo - last in, first out
    Exemplo: pilha de livros adicionando um sobre o outro
Fila (Queue) Fifo - First in, first out
    Exemplo: uma fila real
Filas podem ter efeitos colaterais em desempenho, porque a
cada item alterado, todos os itens sõa modificados
"""
from time import sleep

# Lista
livros = list()
livros.append('Livro 1')
livros.append('Livro 2')
livros.append('Livro 3')
livros.append('Livro 4')
livros.append('Livro 5')
livros.append('Livro 6')
# Remover o último:
print(livros)
livro_removido = livros.pop() # Irá remover o 6

print(livros)

for i in range(2):
    livros.pop()
    print(livros)

# Fila
# Primeiro a entrar é o primeiro a sair
# é melhor não utilizar lista, porque há desempenho colateral nesse ponto

from collections import deque
# Collections é uma possibilidade de estrutura de dados é mais rápida
fila = deque()
fila.append('João')
fila.append('Fernando')
fila.append('Leo')
fila.append('Bernardo')

for nome in fila:
    print(nome)  # Funciona como uma lista no caso

fila.popleft()  # Retira o elemento mais a esquerda
print(fila)

# Podemos também falar que a fila pode ter um tamanho máximo
fila = deque(maxlen=5)  # Tamanho máximo
fila.extend([1, 2, 3, 4])
fila.append(5)
# Após colocar o quinto elemento, ao colocar o sexto elemento, o primeiro é removido

fila = deque(maxlen=10)

for i in range(10):
    fila.append(i)
    print(fila)
    sleep(0.001)

# Insert serve para colocar um valor em determinado índice
fila.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(fila)
try:
    fila.insert(10, 2)  # Somente é possível se a lista não tiver no tamanho máximo
except Exception as error:
    print(error)

fila.appendleft(10)  # Coloca no inicio da fila
print(fila)
# Fila index serve para procurar em qual indice está o objeto
fila.appendleft(100)
print(fila.index(10))