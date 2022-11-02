"""
Getters and Setters
Data: 24/01/2022

"""

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco * (1 - percentual / 100)

# Se o preço for um string, não será possível fazer a mudança
p2 = Produto('Caneca', "R$ 15")
try:
    p2.desconto(10)  # Irá gerar um problema
except:
    pass

# Para evitar problemas, utilizamos getters and setters
# Getter: obtem o valor. Sempre que pedir o valor, esse método será chamado
# Setter: configura o valor. Para usar o setter é necessário utilizar a propriedade do getter

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):  # Estamos checando se o valor é uma classe de string
            valor = float(valor.replace('R$', ''))

        self._preco = valor
        # O valor será o que vai ser atribuido para a variável

    # A vantagem de usar getter e setter é que eu não preciso mexer na estrutura da minha classe

    def desconto(self, percentual):
        self.preco = self.preco * (1 - percentual / 100)

p2 = Produto('Caneca', "R$ 15")
try:
    p2.desconto(10)
    print(f'Novo preço: R$ {p2.preco}')
except:
    pass

# Exemplo com o nome ----
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))

        self._preco = valor

    @property
    def nome(self):
        return self._nome  # No caso, o getter para o nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()  # De forma que as primeiras letras sejam maisculas
        # Setter é como se fosse uma proteção dos atributos

    def desconto(self, percentual):
        self.preco = self.preco * (1 - percentual / 100)