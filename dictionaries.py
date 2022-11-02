"""
Tuples
Data: 27/12/2021

No dicionário, temos sempre uma chave e um valor
"""
# Dicionário vázio
dicionario_vazio = {}
# Exemplo
dicionario_padrao = {'k1': 'v1'}
# Criar nova chave no dicionário
dicionario_padrao['k2'] = 'v2'

# Outra forma de criar um dicionário
dicionario_alternativo = dict(k1='v1', k2='v2')

# Se eu colocar a mesma "key" para um dicionário duas vezes
# ela somente irá considerar a última aplicação da "key"
dicionario_singular = {'k1':1, 'k1':2, 'k1':3}
print(dicionario_singular)

# Para chave, consigo colocar qualquer tipo de dado imutável
exemplo_dicionario = {
    'Fernando': 'String',
    123: 'Numeric',
    (12, 45): 'Tupla'
}
# A chave é uma tupla no caso abaixo
print(exemplo_dicionario[(12, 45)])

# Para evitar erros de utilizar chaves que não existem
if 'Fernando' in exemplo_dicionario:
    print(exemplo_dicionario['Fernando'])
else :
    exemplo_dicionario['Fernando'] = 'String'

# Outra forma é utilizando o get
# Quando utilizamos o get para uma chave que existe,
# retorna o value. Quando utilizamos para uma chave que não
# existe, retorna "None"

print(exemplo_dicionario.get('Fernando'))
print(exemplo_dicionario.get('Ana Luísa'))

# Utilizar o attribute "update" também funciona para atualizar
# valores

# Para checar valores ao inves de chaves, colocamos
# o attribute values
if 'String' in exemplo_dicionario.values():
    print('String is in the dictionary')

# Utilizar o attribute keys retorna o mesmo que não utilizar
# o attribute

# Para acessar as keys e os values, utilizamos items
print(exemplo_dicionario.items())

# Para acessar cada um dos valores e chaves
for k, v in exemplo_dicionario.items():
    print(f'{k}: {v};')

# Desempacotar ----
clientes = {
    'Fernando': {
        'Código': 212241,
        'Data de Nascimento': '1999-07-28',
        'CPF': 12574248660
    },
    'Joana': {
        'Código': 213413,
        'Data de Nascimento': '1963-06-11',
        'CPF': 12314232212,
    }
}

print(clientes)

for nome_cliente, info_cliente in clientes.items():
    print(f'Exibindo cliente: {nome_cliente}.')
    for info_chave, info_valor in info_cliente.items():
        print(f'{info_chave}: {info_valor};')

# Quando dizemos que uma variável é igual a um dicionário
# previamente criado, uma mudança naquela variável também
# muda o respectivo dicionário

clientes_rascunho = clientes
clientes_rascunho['Fernando'] = 'Empty'

print(clientes)

# Para não ter o problema
clientes = {
    'Fernando': {
        'Código': 212241,
        'Data de Nascimento': '1999-07-28',
        'CPF': 12574248660
    },
    'Joana': {
        'Código': 213413,
        'Data de Nascimento': '1963-06-11',
        'CPF': 12314232212,
    }
}

clientes_rascunho = clientes.copy()
clientes_rascunho['Fernando'] = 'Empty'

print(clientes)

# Usar somente o sinal de igual cria uma referência
# Utilizar um copy cria uma cópia rasa, que faz com que o dicionário
# filho possa ser alterado, mas não o primeiro
# Para criar um em que os dicionários filhos não são alteráveis também,
# devemos usar o package copy e usar o deepcopy

lista_nomes = [
    ['Fernando', 22],
    ['Isa', 20],
    ['Bruno', 18]
]

# É possível converter a lista em um dicionário desde que ela tenha a mesma
# formatação de um dicionário

lista_dicionario = dict(lista_nomes)
print(lista_dicionario)
