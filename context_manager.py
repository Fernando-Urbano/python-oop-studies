"""
Context Manager
Data: 01/02/2022

Sempre quando criamos um arquivo e abrimos o arquivo, é necessário fechar o arquivo depois
Fechar o arquivo, pode ser um problema.
Para corrigir o problema, podemos utilizar gereciadores de contexto:
por exemplo, o with
"""

# Forma normal ----
arquivo = open('abc.txt', 'w')
arquivo.write('Algo a ser escrito.')
arquivo.close()

# Forma com gerenciador de contexto ----
with open('abc.txt', 'w') as arquivo:
    arquivo.write('Algo a ser escrito.')


# Com o gerenciador, o arquivo já é fechado no final
# O python permite que você crie os seus próprios

class Arquivo:
    def __init__(self, arquivo, modo):
        print('Objeto criado.')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):  # Somente após usar o método __enter__, a classe se torna gerenciador de contexto
        print('Objeto entrou na classe.')
        return self.arquivo  # Método de entrada

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Objeto saiu na classe.')
        self.arquivo.close()
        # Método de saída


with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('Algo a ser escrito no arquivo.')

# Dessa forma, podemos fazer qualquer coisa que quisermos abrir e depois fechar
# Da mesma, quando queremos liberar e depois soltar, etc.
# exc_type, exc_val e exc_tb servem para caso ocorram excessões
# Podemos tratar a excessão já colocando o return True (irá automaticamente tratar a excessão)


# Fazendo diretamente atraves de função ----
from contextlib import contextmanager


@contextmanager
def abrir(arquivo, modo):
    try:
        print('Abrindo arquivo...')
        arquivo = open(arquivo, modo)
        yield arquivo # tenho que usar yield para ele continuar a executar a função após realizar
    finally:
        print('Fechando arquivo...')
        arquivo.close()

with abrir('abc.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')

# O arquivo escreve entre o try e o finally
# É importante utilizar com with

