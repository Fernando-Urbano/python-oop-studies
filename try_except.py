'''
Try Except
Data: 23/01/2022

Uma excessão faz com que o programa pare
Toda a excessão tem uma classe
'''

try:
    print(a)  # Se alguma parte desse código acontecer,
    # ele irá para o except
except:  # Isso iria para qualquer erro
    pass  # Uma boa prática seria colocar qual tipo de excessão

# Por exemplo:
try:
    print(a)
except NameError as erro:
    print('Erro de desenvolvimento')  # O código irá continuar executando normalmente
except Exception as erro:  # Irá colocar em qualquer outro tipo de erro
    print("Ocorreu um erro inesperado")

try:
    a = []
    print(a[1])
except NameError as erro:
    print('Erro de desenvolvimento')
except IndexError as erro:  # Erro de índice: quando o índice está fora do limite
    print("Erro de índice")
except Exception as erro:  # Irá colocar em qualquer outro tipo de erro
    print("Ocorreu um erro inesperado")

# É possível colocar mais de um tipo de erro:
try:
    a = []
    print(a[1])
except (IndexError, KeyError) as erro:  # Erro de índice: quando o índice está fora do limite
    print("Erro de índice")
else:
    # Executado caso o códio não tiver nenhum problema
    print("Código executado com sucesso")
finally:
    # Vai ser executado independente do sucesso do código
    print('Continuação do código')

# Como tratar excessões
try:
    b = 1/0
except Exception as erro:
    print("Erro.")
finally:
     b = 0

print(b)


