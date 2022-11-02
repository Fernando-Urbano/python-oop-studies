"""
CSV - Comma Separated Values
08/02/2022

"""
import csv

dados = '''
nome, idade, profissao,
Fernando, 22, economista
Fernando, 58, veterinário,
Joana, 57, veterinária,
Ana Luísa, 20, administradora
'''

# Ler base de dados
with open('clientes.csv', 'r') as arquivo:
   dados = csv.reader(arquivo)  # Lê a base de dados
   dados_dict = csv.DictReader(arquivo)  # Lê a base de dados e transforma em dicionário
   # Os dados irão ser organizados de acordo com o a linha e coluna ao qual pertencem

   # No entanto, a operação de dados_dict gera um gerador, portanto, para ter todos os dados, é
   # importante converter em lista
   dados_dict = [x for x in csv.DictReader(arquivo)]

print(dados_dict)

# Criando novo arquivo:
with open('clientes.csv', 'w') as arquivo:
   pass # Isso já irá criar o arquivo

# Criando novo arquivo:
with open('clientes.csv', 'w') as arquivo:
   escrever = csv.writer(  # Escrever é a função de escrever que delimitamos
      arquivo,
      delimiter=',',  # O separador
      quotechar='"',  # Esse o caracter de aspas que vamos usar
      quoting=csv.QUOTE_ALL  # Irá colocar aspas em todos os valores
   )

   # Agora vamos adicionar os valores:
   escrever.writerow(['Nome', 'Sobrenome', 'Idade'])
   escrever.writerow(['Fernando', 'Urbano', '22'])
   escrever.writerow(['Joana', 'Rocha', '57'])
