"""
Create and Modify Packages
Data: 24/01/2022
"""
import json

file = open('abc.txt', 'w+')
# No caso, estamos abrindo um arquivo que não existia previamente. Portanto, ele irá criar o arquivo
# O "w+" se refere a forma como vamos trabalhar o arquivo. No caso, a especificação se refere a poder ler e escrever
# no arquivo

file.write("Linha 1\n")  # Criando linhas no arquivo
file.write("Linha 2\n")
file.write("Linha 3\n")

# Ler nesse mesmo local
print('Lendo linhas:')
print(file.read())
# O problema é que após a terceira linha escrita, o cursor começará a ler a partir do final da terceira linha
# É necessário que o cursor seja movido para o inicio
print("#" * 20)
file.seek(0, 0)  # Posição de onde queremos começar
# Se o segundo número fosse 1, seria relativo a posição do cursor. Com 0, é relativo ao início do arquivo
print(file.read())
# Para ler somente uma linha
file.seek(0, 0)
print(file.readline(), end='')  # end evita a quebra de linhas
print(file.readline(), end='')
print(file.readline(), end='')

# Outra opção:
for linha in file.readlines():
    print(linha, end='')

# É impreensidível fechar o arquivo após terminar de utilizá-lo
file.close()

# Geralmente, pessoas abrem arquivos utilizando
try:
    file = open('abc.txt', 'w+')
    file.write('Linha')
    file.seek(0)  # Para voltar cursor para o inicio
    print(file.read())
finally:
    file.close()

print("\n" + "#" * 20 + "\n" + "Forma Pythonica")

# Forma mais "pythonica" de abrir o arquivo
with open('abc.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0)
    print(file.read())
    # Dessa forma, o arquivo já é fechado quando acabamos de trabalhar com ele

# a+ irá adicionar novas linhas ao inves de reescrever o arquivo
with open("abc.txt", "a+") as file:
    file.write("Linha 4\n")
    file.seek(0)
    print(file.read())

# Apagar o arquivo ----
import os

os.remove("abc.txt")

# Utilizar o json ----
import json

dicionario = {
    12574248660: {
        'nome': 'Fernando Urbano',
        'idade': 22
    },
    16880416715: {
        'nome': 'Ana Martins',
        'idade': 23
    }
}

dicionario_json = json.dumps(dicionario, indent=True)

# É possível criar um json diretamente
with open('abc.json', 'w+') as file:
    file.write(dicionario_json)

with open('abc.json', "r") as file:
    novo_dicionario = json.load(file)  # Dessa forma, o json volta a ser um dicionário

for k, v in novo_dicionario.items():
    print(k)
    for k1, v1 in v.items():
        print(f'{k1}: {v1}')
