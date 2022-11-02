"""
String Template
08/02/2022

Parte de aprender a montar um template em html utilizando módulos do Python.
Essa aula é a base para a aula de enviar e-mail.
Se vamos enviar um e-mail, é possível fazer diretamente com html ou utilizando o template.
Com template, conseguimos personalizar e melhorar a forma como fazemos isso
Criamos o arquivo html.

Dentro do arquivo html, colocamos html e depois clicamos crtl + space
Assim conseguimos algumas possibilidades de html.
No caso, selecionamos a 5.

Colocamos placeholders dentro dos p. O placeholder será depois substituído por o valor que aplicarmos a ele.
<p> </p>

Após fazermos as modificações necessárias no html, vamos abrir o arquivo para pegar o que está dentro dele
"""

from string import Template
import datetime

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime("%d/%m/%Y")
    corpo_msg = template.substitute(nome='Bruno', data=data_atual)  # Para fazer as substituições do que será colocado.
    # Se houver mais um placeholder que não for colocado, haverá exception
    # Para fazer de forma que não levante a excessão, podemos utilizar o safe_substitute
