'''
Create Custom Exceptions
Data: 01/02/2022

Levanta excessões criadas
'''


class Errado(Exception):
    pass  # Criando uma classe que irá ser derivada da classe Exception


def testar():
    raise Errado("Erro!")


try:
    testar()
except Errado as error:
    print(f'Erro: {error}')  # Trato a excessão da forma como eu quiser
