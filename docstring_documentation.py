"""
Docstring Documentation

Serve para documentar o seu código
"""

# Documentação de variável ----
"""Serve para quem utiliza o help() como documentação de uma linha"""
# Isso acima é uma docstring
# A docstring também funciona como uma string multilinhas:
texto = """
Bom dia, Clara,

Gostaria de saber se poderá ir a festa.

Atenciosamente,

Fernando
"""
print(texto)

# Documentação de módulo ----
# Se formos para um módulo mais sério, a documentação geralmente será encontrada nesse formato
"""Título do Modulo

O que o modulo faz...
O que o modulo faz...
O que o modulo faz...
O que o modulo faz...

O que o modulo faz...
O que o modulo faz...
O que o modulo faz...
O que o modulo faz...
"""


# Isso irá aparecer como DESCRIPTION
# É possível estilizar a descrição, colocando negrito, H1, etc.
# Um módulo é um "script"

# Documentação de funções ----
# Sempre que definir a função, a(s) primeira(s) linha(s) da função deverá ser a documentação da função
def soma(x, y):
    """Soma de x e y"""
    return x * y


def soma(x, y):
    """Soma x, y
    
    Soma serve para bla, bla, bla...
    """  # Isso é uma descrição longa da função
    return x * y


# Documentação de funções
def soma_diversos(x, y, z=None):
    """
    Soma x, y

    :param x: Número 1
    :type x: int or float
    :param y: Número 2
    :type y: int or float
    :param z: Número 3 (optional)
    :type z: int, float or None
    
    :return: Soma entre x e y
    :rtype: int or float
    """  # Isso seria uma documentação para explicar os tipos de parametros que devem ser passados
    return x * y if z == None else x * y * z


print(soma_diversos(2, 3))

# Outra forma de ver a documentação de uma função:
print(soma_diversos.__doc__)
print(soma.__doc__)


# O help é mais organizado

# Documentação classes ----
class Cliente:
    """Documentação da Classe"""

    def __init__(self):
        """Iniciar dados (documentação do método)"""
        pass

    def adicionar_nome(self, nome):
        """Criar nome do cliente
        
        :param nome: nome do cliente
        :type: nome: str
        
        :raises ValueError: se o nome..
        """  # raises serve para espeficiar quais excessões o método levanta
        self.nome = nome


print("\n" * 4)
help(Cliente)

# Algumas formas de ajudar a especificar qual o tipo de uma variável
x: int = 10
y: float = 5.5
z: bool = False


def falar(pri_frase: str, seg_frase: str, ter_frase: str, tempo: float = 5):
    return f'{pri_frase}, {seg_frase}, {ter_frase}. Tempo: {tempo}'


falar('Fernando', 5, 5)  # o Pycharm irá me cobrar de colocar de forma diferente


# Falar tipo de retorno dessa função:
def falar(pri_frase: str, seg_frase: str, ter_frase: str, tempo: float = 5) -> str:
    return f'{pri_frase}, {seg_frase}, {ter_frase}. Tempo: {tempo}'

# O "->" só me mostra qual tipo esperamos que a função retorne
# Quando a função pode retornar mais de um tipo de função:
from types import Union

def ler() -> Union(list, dict):
    pass

# O código continuará funcionando mesmo que seja diferente, mas o Pycharm irá "encher o saco"
# De forma que coloque-mos os códigos da forma correta


