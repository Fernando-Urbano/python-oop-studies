"""
While e Else
Data: 26/12/2021
"""

# Utilização do while junto com else possibilita
# utilizar o else quando o while para de ser verdadeiro

soma = 1

while soma <= 5:
    print("Soma: {}".format(soma))
    soma += 1
else:
    print("Processo finalizado.")

# Se um break existir dentro do while, ele não irá passar
# no else
soma = 1

while soma <= 5:
    print("Soma: {}".format(soma))
    soma += 1

    if soma == 5:
        break

else:
    print("Processo finalizado.")

# "+=" com duas strings concatenam as strings