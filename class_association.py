"""
Class Association
Data: 25/01/2022

Relação entre classes:
- Associação: as classes podem viver uma sem a outra

"""


class Escritor:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


esc1 = Escritor('Fernando')


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca


can1 = Caneta('Bic')


class MaquinaDeEscrever:
    pass


maq1 = MaquinaDeEscrever()

# Associando as classes
class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta
    # No caso a ferramenta passará a ser escolhida por fora da classe

    @property
    def nome(self):
        return self.__nome


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print("Caneta está escrevendo...")


class MaquinaDeEscrever:
    def escrever(self):
        print("Máquina está escrevendo...")

# Unindo as classes
escritor = Escritor('Fernando')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()
# Dessa forma estamos enviando a classe inteira para esse atributo da classe escritor
# Essa é associação mais fraca, porque quando o escritor é apagado do programa, a caneta e a maquina
# continuam existindo no programa

del escritor

try:
    print(escritor)
except:
    pass
finally:
    print(caneta.marca)  # Continua existindo
    print(maquina)  # Continua existindo