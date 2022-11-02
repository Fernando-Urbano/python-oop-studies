'''
Calculator Constructiion
15/02/2022

'''

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy


# QSizePolicy irá trazer a possibilidade de os butões se encaixarem


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora em PyQT5')
        # Acima, estamos mudando o nome da janela
        self.setFixedSize(400, 600)
        # Dessa forma, colocamos um formato fixo na calculadora.
        # A calculadora não pode ser aumentada ou redimensionada
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        # Ele irá expandir para ocupar 5 colunas
        # No entanto, se colocarmos assim, a pessoa irá poder digitar na barra
        self.display.setDisabled(True)
        # Dessa forma a pessoa não pode digitar na barra
        self.display.setStyleSheet(
            "* {background: black; color: white; font-size: 30px;}"
        )
        # Estamos definindo o background, a cor e a fonte
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        # O setSizePolicy irá expandir a calculadora para fazer com os botões ocupem tudo dela

        # Primeira Linha:
        self.add_btn(QPushButton('7'), 1, 0, 1, 1)  # Linha 1, Coluna 0
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)  # Linha 1, Coluna 1
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)  # Linha 1, Coluna 2
        self.add_btn(
            QPushButton('*'), 1, 3, 1, 1,
            style='* {background: #b5b6b6; color: white; font-weight: 1400; font-size: 25px}'
        )  # Linha 1, Coluna 3
        self.add_btn(
            QPushButton('C'), 1, 4, 1, 1,
            function=lambda: self.display.setText(''),  # Assim limpamos o display
            style='* {background: darkorange; color: white; font-weight: 1400; font-size: 25px}'
        )  # Linha 1, Coluna 4

        # Segunda Linha:
        self.add_btn(QPushButton('4'), 2, 0, 1, 1)  # Linha 2, Coluna 0
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)  # Linha 2, Coluna 1
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)  # Linha 2, Coluna 2
        self.add_btn(
            QPushButton('-'), 2, 3, 1, 1,
            style='* {background: #b5b6b6; color: white; font-weight: 1400; font-size: 25px}'
        )  # Linha 2, Coluna 3
        self.add_btn(
            QPushButton('←'), 2, 4, 1, 1,
            function=lambda: self.display.setText(
                self.display.text()[: -1]
            ),  # Mantem todos menos o último
            style='* {background: darkorange; color: white; font-weight: 1400; font-size: 25px}'
        )  # Linha 2, Coluna 4

        # Terceira Linha:
        self.add_btn(QPushButton('1'), 3, 0, 1, 1)  # Linha 3, Coluna 0
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)  # Linha 3, Coluna 1
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)  # Linha 3, Coluna 2
        self.add_btn(
            QPushButton('/'), 3, 3, 1, 1,
            style='* {background: #b5b6b6; color: white; font-weight: 1400; font-size: 25px}'
        )  # Linha 3, Coluna 3
        self.add_btn(
            QPushButton('+'), 3, 4, 1, 1,
            style='* {background: #b5b6b6; color: white; font-weight: 1400; font-size: 25px}'
        )  # Linha 4, Coluna 3

        # Quarta Linha:
        # self.add_btn(QPushButton(' '), 4, 0, 1, 1)  # Linha 4, Coluna 0
        self.add_btn(QPushButton('0'), 4, 0, 1, 2)  # Linha 4, Coluna 1
        # self.add_btn(QPushButton(' '), 4, 2, 1, 1)  # Linha 4, Coluna 2
        # self.add_btn(QPushButton('+'), 4, 1, 1, 1)  # Linha 4, Coluna 3
        self.add_btn(
            QPushButton('.'), 4, 2, 1, 1
        )  # Linha 4, Coluna 4
        self.add_btn(
            QPushButton('='), 4, 3, 1, 2,
            function=self.eval_equal,  # Se ele já executasse, teria que ter o ()
            style='* {background: #000000; color: white; font-weight: 1400; font-size: 25px}'
        )  # Linha 4, Coluna 4

        self.setCentralWidget(self.cw)

    def add_btn(self, btn, row, col, rowspan, colspan, function=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        # Acima, cria o botão

        if not function:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(function)
        # Estamos concatenando o que está escrito no botão com o que já estava escrito no display anteriormente
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        btn.setStyleSheet(
            "* {background: #e9e9e9; color: #242424; font-size: 25px;}"
        )

        # Para definir o estilo:
        if style:
            btn.setStyleSheet(style)

    def eval_equal(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )  # eval realiza a operação que fizemos se for possível
        except:
            self.display.setText('Conta invalida.')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
