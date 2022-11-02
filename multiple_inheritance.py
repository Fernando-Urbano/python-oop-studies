"""
Multiple Inheritance
26/01/2022

"""


class A:
    def identificar(self):
        print('Método de Classe A')


class B(A):
    def identificar(self):  # Sobreposição do método
        print('Método de Classe B')


class C(A):
    def identificar(self):  # Sobreposição do método
        print('Método de Classe C')


# Não há ligação entre B e C
# Herança Múltipla
# Classe D herda de B e C
class D(B, C):
    pass


# A classe D tem todos os métodos e atributos de B e C. No entanto, na Classe D temos:
# O Problema do Diamante
# Uma classe herda de duas classes que tem o mesmo método
# No caso do python, ele irá buscar da esquerda para a direita


d1 = D()
d1.identificar()  # Irá herdar de B


class D(C, B):
    pass


d1 = D()
d1.identificar()  # Irá herdar de C


# Exemplo ----
# No caso, estamos usando mixing
class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            return
        self._ligado = True  # O return serve para não fazer o que vem depois dele

    def desligar(self):
        if not self._ligado:
            return
        self._ligado = False  # O return serve para não fazer o que vem depois dele


class Smartphone(Eletronico):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            print(f'{self._nome} não está ligado.')
            return

        if self._conectado:
            print(f'{self._nome} já está conectado.')
            return

        self._conectado = True
        print(f'{self._nome} foi conectado.')

    def desconectar(self):
        if not self._conectado:
            return

        self._conectado = False


# Exemplo
smartphone = Smartphone('IPhone de Joana')
smartphone.desligar()
smartphone.conectar()
smartphone.ligar()
smartphone.conectar()


# Vamos criar arquivo para mostrar quando ocorre erro. Chama-se Log
class LogMixin:
    @staticmethod
    def write(msg):
        with open('log.log', 'a+') as file:
            file.write(msg)
            file.write('\n')
            # a+ serve para adicionar mais linhas ao arquivo
        # Tendo em vista que não utilizamos a palavra self em momento algum esse método pode se tornar estático
        # Por isso, o @staticmethod

    def log_info(self, msg):
        self.write(f'INFO: {msg}')

    def log_error(self, msg):
        self.write(f'ERROR: {msg}')


# Até então, a classe LogMixin não tem nada referente a Smartphone ou Eletronico
# Mas agora faremos a heranã multipla:


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            error = f'{self._nome} não está ligado.'
            print(error)
            self.log_error(error)
            return

        if self._conectado:
            error = f'{self._nome} já está conectado.'
            print(error)
            self.log_error(error)
            return

        self._conectado = True
        info = f'{self._nome} foi conectado.'
        print(info)
        self.log_info(info)

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} não está conectado.'
            print(error)
            self.log_error(error)
            return

        self._conectado = False
        info = f'{self._nome} foi desconectado.'
        print(info)
        self.log_info(info)


# Se o método write tiver self, não irá funcionar
smartphone = Smartphone('IPhone de Joana')
smartphone.desligar()
smartphone.conectar()
smartphone.ligar()
smartphone.conectar()
smartphone.conectar()
smartphone.desligar()
smartphone.conectar()
smartphone.ligar()

# Importante lembrar do Mixing