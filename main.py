import sys
from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
janela = QWidget()

janela.resize(500,400)
janela.setWindowTitle('Primeira janela.')
janela.show()

app.exec()

