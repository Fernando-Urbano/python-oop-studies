"""
os
07/02/2022

"""
import os

# Módulo 'os'
caminho_procurar = r"C:\Users\ferna\OneDrive\Área de Trabalho\Fotos"
termo_procurar = '0'

numero_arquivos = 0
for raiz, diretorios, arquivos in os.walk(caminho_procurar):
    for arquivo in arquivos:
        try:

            caminho_completo = os.path.join(raiz, arquivo)
            print(caminho_completo)
            nome_arquivo, ext_arquivo = os.path.splitext(caminho_completo) # Mostra a extensão separada
            print(nome_arquivo, '-', ext_arquivo)
            nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
            print(nome_arquivo, '-', ext_arquivo)
            tamanho = os.path.getsize(caminho_completo)
            # Mostra o tamanho do arquivo
            print(tamanho)  # Estará em bites

            print(arquivo)
            numero_arquivos += 1
            # Procurar arquivos com termo:
            if termo_procurar in arquivo:
                print('Arquivo contem padrão')
        except PermissionError and FileNotFoundError as error:
            print(error)

# Algumas excessões comuns:
# - PermissionError
# - FileNotFoundError

print(f'Número de arquivos encontrados: {numero_arquivos}.')


def listdir(param):
    return None