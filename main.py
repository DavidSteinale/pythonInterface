import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel

app = QApplication(sys.argv)
janela = QWidget()
botao = QPushButton('Botão 1',janela) #Define um objeto button, com o nome e a janela queira usar
label = QLabel('TEXTO', janela) # cria texto

janela.resize(300,300) # Define o tamanho da janela
janela.setWindowTitle('Primeira janela.') # texto que aparece no topo da janela
botao.setGeometry(100,25,100,25) # colocado antes do show() , é informado a posição do button o SetGeometry
botao.setStyleSheet('color:black; background:yellow; font-weight: 900') # style o botão com CSS
label.move(100,50) # posição na janela


janela.show() #mostra a janela

app.exec() # manda executar a aplicação.

