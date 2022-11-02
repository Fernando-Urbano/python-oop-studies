'''
Create Except
Data: 23/01/2022

Levantando as excessões
'''


def dividir(n1, n2):
    return n1 / n2
    # Se n2 for 0, haverá um problema

# Como corrigir
def dividir_correto(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print('Log: ', error)
        return False  # Você relança a excessão

print(dividir_correto(2, 0))

# Como colocar
def dividir_correto(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print('Log: ', error)
        raise ValueError("n2 não pode ser 0.")
        # Você relança o erro, mas após fazer o que você quiser
        # e colocando a mensagem personalizada

try:
    print(dividir_correto(2, 0))
except ValueError as error:
    print(error)





