'''
Calculator Constructiion
15/02/2022

'''

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy


class AnnotateSales(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Anotação de Vendas')
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.setFixedSize(400, 300)
        self.card_types = ['Alimentação', 'Crédito', 'Débito']
        self.card_companies = ['Visa', 'Mastercard', 'Alelo', 'Sodexo']

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 3)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            "* {background: black; color: white; font-size: 30px;}"
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.setCentralWidget(self.cw)

        self.add_btn_type(QPushButton('Alimentação'), 1, 0, 1, 1, card_type=True)
        self.add_btn_type(QPushButton('Crédito'), 1, 1, 1, 1, card_type=True)
        self.add_btn_type(QPushButton('Débito'), 1, 2, 1, 1, card_type=True)

        column_index = 0
        row_index = 2
        for card_company in self.card_companies:
            self.add_btn_type(QPushButton(card_company), row_index, column_index, 1, 1)
            if column_index < 2:
                column_index += 1
            else:
                row_index += 1
                column_index = 0

    def add_btn_type(self, btn, row, col, rowspan, colspan, card_type=False):
        self.grid.addWidget(btn, row, col, rowspan, colspan)

        if card_type:
            btn.setStyleSheet(
                "* {background: #ebebeb ; color: #000000; font-size: 20px; font-family: 'Trebuchet MS'; font-weight: "
                "bold; border: 0px double red} "
            )
            btn.clicked.connect(
                lambda: self.activate_card_type_btn(btn)
            )
        else:
            btn.setStyleSheet(
                "* {background: #ff9300 ; color: #ffffff; font-size: 20px; font-family: 'Trebuchet MS'; font-weight: "
                "bold; border: 0px double red} "
            )
            btn.clicked.connect(
                lambda: self.activate_card_company_btn(btn)
            )

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def activate_card_type_btn(self, btn):
        new_text = self.display.text().replace(' - ', '')
        for card_type in self.card_types:
            new_text = new_text.replace(card_type, '')

        if len(new_text) > 0:
            self.display.setText(
                btn.text() + ' - ' + new_text
            )
        else:
            self.display.setText(
                btn.text()
            )

    def activate_card_company_btn(self, btn):
        new_text = self.display.text().replace(' - ', '')
        for card_company in self.card_companies:
            new_text = new_text.replace(card_company, '')

        if len(new_text) > 0:
            self.display.setText(
                new_text + ' - ' + btn.text()
            )
        else:
            self.display.setText(
                btn.text()
            )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = AnnotateSales()
    calc.show()
    qt.exec_()
