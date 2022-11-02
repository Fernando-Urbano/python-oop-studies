"""
Webscraping
13/02/2022

É necessário ter noção de HTML e CSS. Cada site terá um diferente
"""
import requests
from bs4 import BeautifulSoup
# O request é capaz de baixar os dados e o beautifulsoup4 (bs4) permite que manipulemos os dados
# dentro do python

# Conseguindo a url
url = 'https://pt.stackoverflow.com/questions/tagged/python'
# response é utilizado para obter os dados da url
response = requests.get(url)
# print(response.text)

# Se formos usar "post", é necessário colocar o parametro "data" com os dados para o post
html = BeautifulSoup(response.text, 'html.parser')
# Beautiful soup irá servir reenderizar nosso html.
# É importante dizer que estamos tratando de um html
# print(html)
# Depois, para ver o html no site, clicamos com o botão direito no site
# e após inspecionar

for pergunta in html.select('.question-summary'):
    # print(pergunta)
    # printar a pergunta irá gerar um html
    # O html.select é um css.
    # Na pergunta, conseguimos fazer o html select novamente.
    # Na pergunta, temos um título
    titulo = pergunta.select_one('.question-hyperlink')
    # Select_one me parece ser para selecionar o primeiro objeto.
    # O titulo ainda é um html, para selecionar somente o texto do título é necessário
    # colocar .text no final

# O site mudou, então a forma antiga não funciona mais
for pergunta in html.select('.s-link'):
    print(pergunta.text)

for pergunta in html.select('.s-post-summary--content'):
    tempo = pergunta.select_one('.s-user-card--time')
    titulo = pergunta.select_one('.s-link')
    print(f'{tempo.text}: {titulo.text}')

for pergunta in html.select('.s-post-summary--stats-item-number mr4'):
    print('found')
