'''
PyQT

PyQT é um toolkit desenvolvido em C++ utilizado por vários programas para criação de aplicações GUI
(Interface Gráfica). Também inclui diversas funcionalidades, como: acessar a base de dados, threads, comunicação
de rede, etc...
'''
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout

class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton('Texto do Botão')  # Definir a existência do botão
        self.btn.setStyleSheet('font-size: 40px;')  # define a aparência do botão
        # no caso, estamos falando do tamanho da letra
        self.grid.addWidget(self.btn, 0, 0, 1, 1)
        # Toda vez que colocamos um grid devemos especificar, além do objeto que estamos colocando
        # qual a linha (primeiro 0), quala a coluna (segundo 0), e
        # quantas linhas e colunas esse botão irá ocupar.
        # (terceiro e quarto número)
        self.setCentralWidget(self.cw)  # Coloca o botão no meio da aplicação

        # No entanto, até aqui, quando clicamos no botão, nada acontece.
        # É necessário colocar um clicked e dentro desse clicked passar um método da classe
        # Se for muito pequeno, pode ser uma função anonima (por exemplo, lambda)
        self.btn.clicked.connect(lambda: print('Olá mundo!'))
        # O print será na saída do terminal

        # para jogar o método
        self.btn.clicked.connect(self.realizar_acao)

    def realizar_acao(self):
        print('Ação realizada!')



if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()  # Somente de fazer isso, já vamos ter uma janela na tela






