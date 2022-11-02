"""
Datetime
07/02/2022

"""
from datetime import datetime, timedelta

data = datetime(2022, 2, 7, 22, 11, 2)
# Ano, mês, dia, hora (opcional), minuto (opcional), segundo (opcional)
print(data)

# Como formatar a data?
print(data.strftime("%d/%m/%Y"))
print(data.strftime("%b/%Y"))
print(data.strftime("%d/%m/%Y %H:%M:%S"))

# String para data ----
data = datetime.strptime("20/04/2022", "%d/%m/%Y")
print(data)  # Retornará uma data

# Timestamp serve para contar segundos desde 1970
print(data.timestamp())

print(datetime.fromtimestamp(1023024))  # Parte no primeiro dia de 1970

# timedelta: diferença de tempos ----
d1 = datetime(2022, 2, 10, 22, 10, 2)
d1 = d1 + timedelta(days=10)  # Adicionar 10 dias
d1 = d1 + timedelta(seconds=55)  # Adicionar segundos
d1 = d1 + timedelta(hours=24)

d2 = datetime(2022, 2, 28, 9, 30, 00)
dif = d2 - d1
print(dif)
print(dif.seconds)  # Mostra os segundos naquela hora
print(dif.total_seconds())  # Mostra todos os segundos
print(dif.days)
print(d2.time())  # Mostra somente a hora

# Possível comparar datas
print(d1 == d2)
print(d2 > d1)

# Datas em Português ----
# Sexta, 13 de Junho de 2018
# Necessário adicionar outro módulo
d1 = datetime.now()
formatacao = d1.strftime("%A, %d de %B de %Y")
print(formatacao)
# Como colocar em português
from locale import setlocale, LC_ALL
setlocale(LC_ALL, '')  # Se eu colocar uma ‘string’ vazia, ele vai colocar no mesmo local do computador
setlocale(LC_ALL, 'pt_BR.utf-8')  # Como colocar em português BR.
formatacao = d1.strftime("%A, %d de %B de %Y")
print(formatacao)
print(datetime.now().strftime("%b/%Y"))

# Pegar o último dia do mês ----
from calendar import mdays
# Necessário calendar

mes_atual = int(datetime.today().strftime("%m"))
print(mes_atual, mdays[mes_atual])  # Necessário colocar como ‘string’


