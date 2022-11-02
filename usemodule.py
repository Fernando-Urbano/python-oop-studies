"""
Create Modules
Data: 23/01/2022
"""

def dobrar_lista(lista):
    return [x*2 for x in lista]

lista = list(range(3, 10))
print(dobrar_lista(lista))

import math

PI = math.pi  # Uma variável que não muda o seu valor é geralmente escrita com letras

if __name__ == "__main__":
    print(dobrar_lista(lista))
    print(__name__)
    # Somente irá rodar isso se eu rodar esse código. Se eu rodar um código que chama esse código,
    # ele não irá rodar