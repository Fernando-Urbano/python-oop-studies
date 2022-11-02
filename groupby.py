'''
Groupby
Data: 23/01/2022

Agrupa dados de um dicionário
'''

alunos = [
    {'nome': 'Joana', 'nota': 10},
    {'nome': 'Bruno', 'nota': 8},
    {'nome': 'Bia', 'nota': 8},
    {'nome': 'João', 'nota': 7},
    {'nome': 'Cristiano', 'nota': 3},
    {'nome': 'André', 'nota': 3},
    {'nome': 'Leonardo', 'nota': 8},
]
# Ordenando dicionário
alunos.sort(key=lambda item: item['nota'])
print(alunos)

# Ordenando do maior para o menor
alunos.sort(key=lambda item: -item['nota'])
print(alunos)

# Agrupando os alunos
import itertools
alunos_agrupados = itertools.groupby(alunos, lambda item: item['nota'])
print(alunos_agrupados)

for agrupamento, valores_agrupados in alunos_agrupados:
    m_var, n_var = itertools.tee(valores_agrupados)
    print(f'Agrupamento: {agrupamento}')

    numero_alunos = len(list(n_var))

    print(f'{numero_alunos} receberam essa nota') if numero_alunos > 1 else print(f'{numero_alunos} recebeu essa nota')

    for aluno in valores_agrupados:
        print(aluno)
    print(" ")
