"""
Validade a CNPJ
Data: 24/01/2022


"""
from functools import reduce

cnpj_to_validade = str(input("CPNJ: "))

if len(cnpj_to_validade) == 12:

    numbers_cnpj_to_validade = []

    for character in cnpj_to_validade:
        if len(numbers_cnpj_to_validade) < 10:
            try:
                character = int(character)
                numbers_cnpj_to_validade.append(character)
                print(character, end='  ')
            except:
                pass

    print()
    numbers = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4]
    for number in numbers:
        print(number, end='  ')

    print()
    validation = zip(numbers_cnpj_to_validade, numbers)

    validation_list = []
    for cnpj_n, n in validation:
        validation_list.append(cnpj_n * n)

    for i in range(len(validation_list)):
        if validation_list[i] > 9 or i == len(validation_list) - 1:
            print(validation_list[i], end=' ')
        else:
            print(validation_list[i], end='  ')

    sum_validation = reduce(lambda acumulador, i: i + acumulador, validation_list, 0)
    result = 11 - (sum_validation % 11)

    print('=',sum_validation)
    print()
    print(f'11 - ({sum_validation} % 11) = {result}')
    print()
    result = result if result < 10 else 0
    print(f'Primeiro dígito: {result}')

    # Resultado com primeiro dígito após "/"
    numbers_cnpj_to_validade.append(result)

    numbers = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4]
    for number in numbers:
        print(number, end='  ')

    print()
    validation = zip(numbers_cnpj_to_validade, numbers)

    validation_list = []
    for cnpj_n, n in validation:
        validation_list.append(cnpj_n * n)

    for i in range(len(validation_list)):
        if validation_list[i] > 9 or i == len(validation_list) - 1:
            print(validation_list[i], end=' ')
        else:
            print(validation_list[i], end='  ')

    sum_validation = reduce(lambda acumulador, i: i + acumulador, validation_list, 0)
    result = 11 - (sum_validation % 11)

    print('=', sum_validation)
    print()
    print(f'11 - ({sum_validation} % 11) = {result}')
    print()
    result = result if result < 10 else 0
    print(f'Segundo dígito: {result}')

    # Resultado com segundo dígito após "/"
    print()
    numbers_cnpj_to_validade.append(result)

    print("CNPJ Correto:")
    for number in numbers_cnpj_to_validade:
        print(number, end='')

    numbers_cnpj_writen = []
    print()
    print("CNPJ Escrito:")
    for character in cnpj_to_validade:
        try:
            character = int(character)
            numbers_cnpj_writen.append(character)
            print(character, end='')
        except:
            pass

    print()
    if numbers_cnpj_writen[10] == numbers_cnpj_to_validade[10] and numbers_cnpj_writen[11] == numbers_cnpj_to_validade[11]:
        print("CNPJ válido.")
    else:
        print("CNPJ inválido")

else:
    print("CNPJ inválido")




