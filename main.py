import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

def funcao1():
    label.setText('Bem vindo a primeria janela grafica')
    label.adjustSize()

def funcao2():
    valor_lido = le.text()
    if (valor_lido=='david'):
        label.setText(f"Login efetuado com sucesso Sr {valor_lido}")
        label.adjustSize()
    else:
        label.setText("Login não aceito")
        label.adjustSize()

def funcao3():
    janela2.resize(300,200) # Define o tamanho da janela
    janela2.setWindowTitle('Menu Cadastro de fornecedor')  # texto que aparece no topo da janela.
    janela2.show()


app = QApplication(sys.argv)
janela = QWidget()
janela2 = QWidget()
botao = QPushButton('Botão 1',janela) #Define um objeto button, com o nome e a janela queira usar
botao2 = QPushButton('Botão 2',janela) #Define um objeto button, com o nome e a janela queira usar
botao3 = QPushButton('Botão 3',janela) #Define um objeto button, com o nome e a janela queira usar
label = QLabel('TEXTO', janela) # cria texto

janela.resize(600,300) # Define o tamanho da janela
janela.setWindowTitle('Primeira janela.') # texto que aparece no topo da janela

botao.setGeometry(100,25,100,25) # colocado antes do show() , é informado a posição do button o SetGeometry
botao2.setGeometry(100,50,100,25) # colocado antes do show() , é informado a posição do button o SetGeometry
botao3.setGeometry(100,75,100,25) # colocado antes do show() , é informado a posição do button o SetGeometry
# botao.setStyleSheet('color:black; background:green; font-weight: 900') # style o botão com CSS
botao.clicked.connect(funcao1)
botao2.clicked.connect(funcao2)
botao3.clicked.connect(funcao3)

label.setStyleSheet('font-size:30px')
label.move(100,100) # posição na janela

le = QLineEdit("",janela)
le.setGeometry(300,25,150,25)

janela.show() #mostra a janela

app.exec() # manda executar a aplicação.

