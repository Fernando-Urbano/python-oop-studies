"""
Sys.argv - Running Scripts in System
09/02/2022

Abro o terminal.
No windows, colocamos "python" no terminal e assim ele entra no terminal do python.
Caso necessário, é possível falar qual versão do python eu gostaria de utilizar. Por exemplo: python3.7
Para mudar a pasta em que estamos:

cd "Nome da pasta a adicionar".

Dentro do anaconda prompt está funcionando!

Como executar o script
C:\Users\ferna\PycharmProjects\Python Course Udemy\Outside Modules> python hello_world_file.py

"""
import sys
import os

argumentos = sys.argv
# Retorna os argumentos que foram passados no terminal
print(argumentos)

# Continua em sys_argv...
