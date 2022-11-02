'''
Training Dictionnaries
Data: 06/01/2022

'''

perguntas = {
    'Pergunta 1': {
        'Pergunta': 'Quanto é 2+2?',
        'Respostas': {
            'a': '1',
            'b': '2',
            'c': '4',
        },
        'Resposta Certa': 'c'
    },
    'Pergunta 2': {
        'Pergunta': 'Quanto é 3+3?',
        'Respostas': {
            'a': '5',
            'b': '3',
            'c': '6',
        },
        'Resposta Certa': 'c'
    },
}

numero_acertos = 0
numero_perguntas = 0

# Iterar sobre as perguntas
for pergunta_key, pergunta_value in perguntas.items():
    print(f'{pergunta_key}: {pergunta_value["Pergunta"]}')

    # Acessar as respostas
    print('Escolha a resposta desejada pela letra:')
    for resp_key, resp_value in pergunta_value["Respostas"].items():
        print(f'{resp_key}) {resp_value}')

    resposta_usuario = input('Resposta escolhida: ')
    if resposta_usuario == pergunta_value['Resposta Certa']:
        print('Resposta correta.')
        numero_acertos += 1
    else:
        print('Resposta errada.')

    numero_perguntas += 1

print('Acertos:', numero_acertos, '/', numero_perguntas)

