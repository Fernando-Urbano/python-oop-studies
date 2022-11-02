"""
Class Attributes
Data: 25/01/2022

"""


class Basica:
    variavel_basica = 100


a1 = Basica()
a2 = Basica()
a3 = Basica()
print(a1.variavel_basica)
# variavel_basica é uma variável de classe que está disponível para todas as instâncias

# Além disso, tendo em vista que a variável é de classe, uma mudança na variável gera uma mudança em todas
# as instâncias
Basica.variavel_basica = 200  # Isso acontece porque é uma variável de classe
print(a1.variavel_basica)
print(a2.variavel_basica)
print(a3.variavel_basica)
# No entanto, não é possível utilizar a instância para alterar a variável de classe
a1.variavel_basica = 300
# Não irá alterar a variavel_basica na classe
print(a2.variavel_basica)  # Continua sendo 200
# Na verdade, ao fazermos isso criamos um dicionário dentro da variável
print(a1.__dict__)  # Aparecerá o dicionário criado
print(a2.__dict__)  # Não aparecerá nada


# No caso do a2, ele começa buscando pela instância, ao não achar nada ele procura na classe

# E quando as variáveis de classe e de atributo são as mesmas?
# Por exemplo:
class BasicaAtributo:
    var = 100

    def __init__(self):
        self.var = 200


b1 = BasicaAtributo()
print(b1.var)

BasicaAtributo.var = 400
print(b1.var)  # Não irá mudar
# É necessário que o atributo não tenha o "var" para que mude


class BasicaAtributo:
    var = 100

    def __init__(self):
        pass


b1 = BasicaAtributo()
print(b1.var)
BasicaAtributo.var = 400
print(b1.var)  # Agora mudou


