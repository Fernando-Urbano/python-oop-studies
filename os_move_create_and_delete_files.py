"""
os Move, Delete, Create Files
08/02/2022

"""
import os
import shutil

caminho_original = r"C:\Users\ferna\OneDrive\Área de Trabalho"
caminho_novo = r"C:\Users\ferna\OneDrive\Área de Trabalho\Nova Pasta"

try:
    os.mkdir(caminho_novo) # Cria nova pasta
except FileExistsError as error:
    pass

numero_arquivos = 0
for root, dirs, files in os.walk(caminho_original):
    for file in files:
        if file == "File que não existe":
            old_file_path = os.path.join(root, file)  # Colocando
            new_file_path = os.path.join(caminho_novo, file)
            print(old_file_path)
            shutil.move(old_file_path, new_file_path)  # Move os arquivos
            # O move também serve pare renomear, caso necessário
            shutil.copy(old_file_path, new_file_path)  # Ele irá copiar os arquivos
            os.remove(new_file_path)  # Remove o arquivo
        numero_arquivos += 1
print(numero_arquivos)


