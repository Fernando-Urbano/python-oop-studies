"""
Decorators and Decorator Functions
Data: 24/01/2022

Assunto relativamente complexo
"""


def falar_ola():
    print("Olá!")


variavel = falar_ola
# Se eu usar a "variavel" dessa forma, a variavel passa a fazer a mesma função da função
print(type(variavel))


def master():  # Função master
    def slave():  # Função dependente da função master
        print("Olá!")

    slave()  # A master cria e executa a slave


master()


def master():  # Função master
    def slave():  # Função dependente da função master
        print("Olá!")

    return slave


# Agora a master vai retornar a função. Se falarmos que a variavel é igual a master(),
# variável agora será uma função
variavel = master()
print(type(variavel))

# Podemos criar uma função master que executa a função slave que é igual a função que tratamos antes
# Aqui começamos a tratar a ideia de função decoradora
print('\n')


def master(funcao):
    def slave():
        funcao()

    return slave


falar = master(falar_ola)
falar()


# Outra forma de decorar:
@master  # Assim é a forma mais comum de decorar
def falar_ola():
    print("Olá!")


# Caso a função receber parametros, seria a mesma ideia que a slave ter *args e **kargs
def master(funcao):
    def slave(*args, **kargs):
        funcao(*args, **kargs)

    return slave


# Exemplo ----
from time import time
from time import sleep


def velocidade(funcao):
    def interna(*args, **kargs):
        start_time = time()
        resultado_interna = funcao(*args, **kargs)
        end_time = time()
        function_time = end_time - start_time
        print(f'\n\nA função "{funcao.__name__}" demorou {function_time:.3f} segundos para ser executada.')
        return resultado_interna

    return interna


@velocidade
def demorar():
    for i in range(5):
        print(i, end=' ')
        sleep(0.1)

# A função velocidade é utilizada para definir quanto temp a outra função demorou para ser executada
demorar()
