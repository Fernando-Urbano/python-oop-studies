"""
Threads Parallel Processing
15/02/2022

Como fazer execuções paralelas.
Isso é uma forma de executar o código de forma não linear.
Podemos utilizar a main thread para mandar outras threads fazerem serviços
para mim
"""
from time import sleep
from threading import Thread

# Thread é uma classe

if __name__ != '__main__':
    class MeuThread(Thread):
        def __init__(self, texto, tempo):
            super().__init__()
            self.texto = texto
            self.tempo = tempo
            # Vai exibir um texto depois de um tempo

        def run(self):
            sleep(self.tempo)
            print(self.texto)
            sleep(self.tempo)
            print(self.texto)


    t1 = MeuThread('Thread 1', 5)
    # Assim estamos criando uma subthread
    t1.start()

    t2 = MeuThread('Thread 2', 3)
    t2.start()
    # Start é um método da classe Thread

    t3 = MeuThread('Thread 3', 3)
    t3.start()

    # A partir do momento que colocamos a thread para startar,
    # ela começa a rodar o que temos de métodos dentro da thread

    for i in range(20):
        print(i)
        sleep(1)



    # Outra forma de criar Threads:
    def vai_demorar(texto, tempo):
        sleep(tempo)
        print(texto)



    t1 = Thread(target=vai_demorar, args=('Olá mundo 1', 5))
    t1.start()

    t2 = Thread(target=vai_demorar, args=('Olá mundo 2', 3))
    t2.start()

    t3 = Thread(target=vai_demorar, args=('Olá mundo 3', 1))
    t3.start()

    for i in range(20):
        print(i)
        sleep(.5)

    # Para pausar dentro de uma thread
    t1 = Thread(target=vai_demorar, args=('Olá mundo!', 8))
    t1.start()

    i = 0
    while t1.is_alive():
        print('Esperando a thread...')
        sleep(1)

    print('Thread acabou...')
    # Se fizermos join, a thread passa para a thread principal,
    # assim fazendo parte do processo como o resto do código
    t1.join()


# Thread podem gerar problemas, dado que pode haver falta de sincronia
class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque

    def comprar(self, quantidade):
        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            return

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingressos. Ainda temos {self.estoque}.')


# Se duas pessoas tentarem comprar ingressos em conjunto, haverá um problema
# elas podem conseguir comprar os ingressos porque a função de comprar terminou para um enquanto
# não terminou para outro
if __name__ == '__main__':
    ingressos = Ingressos(10)

    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()


# No caso, ainda funcionou, mas se colocarmos um sleep, não irá mais funcionar...
class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque

    def comprar(self, quantidade):
        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            return

        sleep(1)

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingressos. Ainda temos {self.estoque}.')


if __name__ == '__main__':
    ingressos = Ingressos(10)

    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()
    # Elas reduziram depois de ter passado self.estoque

# Para resolver o problema, utilizamos locks
from threading import Lock


class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()  # Ao entrar no método, ele irá trancar

    def comprar(self, quantidade):
        self.lock.acquire()  # Trancou o método pelo lado de dentro
        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            self.lock.release()  # Liberou o método para ser executado por outros...
            return

        sleep(1)

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingressos. Ainda temos {self.estoque}.')
        self.lock.release()  # Liberou o método para ser executado por outros...


if __name__ == '__main__':
    ingressos = Ingressos(10)

    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()