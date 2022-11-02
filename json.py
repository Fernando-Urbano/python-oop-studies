"""
JSON - JavaScript Object Notation
08/02/2022
JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas e programas muito leve e de
fácil utilização. Muito utilizado por APIs.

De Python para JSON:
dict > object
list, tuple > array
str > string
int, float > number
True > true
False > false
None > null

De JSON para Python:
object > dict
array > list
string > str
number (int) > int
number (real) > float
true > True
false > False
null > None
"""
import json

lista = list(range(9))
print(lista)
nome = 'Fernando Corrêa'

# Converter Python em JSON:
dados_json = json.dumps(lista)
print(dados_json)
print(f'Tipo: {type(dados_json)}')

dados_json = json.dumps(nome)
print(dados_json)
print(f'Tipo: {type(dados_json)}')

# Mostrando um dicionário convertido em JSON de forma melhor:
dados = {
    1: {
        'Nome': 'Fernando',
        'Sobrenome': 'Urbano'
    },
2: {
        'Nome': 'Joana',
        'Sobrenome': 'Urbano'
    },
3: {
        'Nome': 'Bruno',
        'Sobrenome': 'Urbano'
    },
}
print(dados)
dict_json = json.dumps(dados, indent=4)  # Faz a identação de forma a ficar mais visível
print(dict_json)
print(type(dict_json))

# Converter JSON para Python:
dicionario = json.loads(dict_json)
print(dicionario)
for key, value in dicionario.items():
    print(key)
    for subkey, subvalue in value.items():
        print(f'{subkey}: {subvalue}')
    print('\n')

# Convertemos em json:
with open('clientes.json', 'w') as arquivo:
    json.dump(dicionario, arquivo, indent=4)  # Já coloca o json no arquivo

# Convertermos em python:
with open('clientes.json', 'r') as arquivo:
    dados = json.load(arquivo)

for key, value in dados.items():
    print(key)
    for subkey, subvalue in value.items():
        print(f'{subkey}: {subvalue}')
    print('\n')