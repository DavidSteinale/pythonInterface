import sys
from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
janela = QWidget()

janela.resize(500,400) # Define o tamanho da janela
janela.setWindowTitle('Primeira janela.') # texto que aparece no topo da janela
janela.show() #mostra a janela

app.exec() # manda executar a aplicação.

