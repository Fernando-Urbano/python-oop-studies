'''
Modules
Data: 23/01/2022

Módulos padrão do Python:
Módulos são arquivos .py (que contem código python) e servem para expandir as funcionalidades padrão da linguagem.
'''
import sys  # No caso sys é um modulo

# print(sys.) - Com isso consigo saber o que tem dentro do modulo

print(sys.platform)  # Ver em qual plataforma está sendo utilizado

# O mesmo funciona
from sys import platform

print(platform)  # Não é necessário colocar o módulo

import random
for i in range(10):
    print(random.randint(0, 1))

from random import * #  Você importa tudo do módulo random
print(randint(0, 1))

# 
