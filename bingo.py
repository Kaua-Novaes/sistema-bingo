from itertools import count
import sys #importando ferramentas do sistema
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QTextEdit
from PyQt6.QtGui import QPixmap
from PyQt6.QtGui import QMovie
import random 
from PyQt6.QtCore import pyqtSlot



app = QApplication(sys.argv)

with open('style.css','r') as file: 
    app.setStyleSheet(file.read())

#janela
login = QWidget()
login.resize(900,800)
login.setWindowTitle('Login!')
login.setObjectName('janela')

#titulo
titulo1 = QLabel('Bingo',login)
titulo1.move(190,250)
titulo1.setStyleSheet('color:rgb(255, 0, 187); font-size:100px; font-family:"Blippo", fantasy; font-weight: bold')
#titulo2
titulo2 = QLabel('.bet',login)
titulo2.setStyleSheet('color:white; font-size:100px; font-family:"Blippo", fantasy; font-weight: bold')
titulo2.move(470,250)

def iniciar():
    janela.show()
    login.close()



#começar
startGame = QPushButton('COMEÇAR',login)
startGame.setGeometry(295, 400,280,50)
startGame.setObjectName('botaoSort')
startGame.clicked.connect(iniciar)

#roleta
esqueleto = QLabel('',login)
esqueleto.movie = QMovie("login.gif")
esqueleto.setMovie(esqueleto.movie)
esqueleto.movie.start()
esqueleto.move(280,435)


login.show()


#janela
janela = QWidget()
janela.resize(900,800)
janela.setWindowTitle('Login!')
janela.setObjectName('janela')


#titulo
titulo1 = QLabel('Bingo',janela)
titulo1.move(300,20)
titulo1.setStyleSheet('color:rgb(255, 0, 187); font-size:60px; font-family:"Blippo", fantasy; font-weight: bold')
#titulo2
titulo2 = QLabel('.bet',janela)
titulo2.setStyleSheet('color:white; font-size:60px; font-family:"Blippo", fantasy; font-weight: bold')
titulo2.move(470,20)


#borda bolinhas sorteadas
info = QLabel('',janela)
info.setStyleSheet('border-radius:3px; background-color:white; font-size: 40px;')
info.setGeometry(290,120,283,250)



lista1 = []
lista2 = []

info = 0

texto = QLineEdit('')



def criar():
    global contador
    global info
    global lista2
    for i in range(1,999):
        sorte = random.randint(1,75)
        if sorte not in lista2:
            lista2.append(sorte)
    x = 0
    y = 440
    global v1
    print(lista2)
    for i in range(1,6): 
        if i <= 1:
            for j in range(1,16):
                x = x + 52
                v1 = QLineEdit(f'  {j} ',janela)
                v1.setObjectName('sorteados')
                v1.setGeometry(x,y,49,33)
                v1.setFixedSize(49,33)
                v1.move(x,y)
                v1.show()
            x = 0
        elif i <= 2:
            for p in range(16,31):
                x = x + 52
                v1 = QLineEdit(f'  {p} ',janela)
                v1.setObjectName('sorteados')
                v1.setGeometry(x,477,49,33)
                v1.setFixedSize(49,33)
                v1.move(x,477)
                v1.show()
            x = 0
        elif i <= 3:
            for l in range(31,46):
                x = x + 52
                v1 = QLineEdit(f'  {l} ',janela)
                v1.setObjectName('sorteados')
                v1.setGeometry(x,514,49,33)
                v1.setFixedSize(49,33)
                v1.move(x,514)
                v1.show()
            x = 0
        elif i <= 4:
            for a in range(46,61):
                x = x + 52
                v1 = QLineEdit(f'    {a} ',janela)
                v1.setObjectName('sorteados')
                v1.setFixedSize(49,33)
                v1.move(x,551)
                v1.show()  
            x = 0
        elif i <= 5:
            for b in range(61,76):
                x = x + 52
                v1 = QLineEdit(f'    {b} ',janela)
                v1.setObjectName('sorteados')
                v1.setFixedSize(49,33)
                v1.move(x,588)
                v1.show()    
            x = 0
        num.setText('')
        numSequencia.setText('')
        texto.setText('')
        if btncomecar.text() == 'encerrar':
            lista2 = []
            for i in range(1,999):
                sorte = random.randint(1,75)
                if sorte not in lista2:
                    lista2.append(sorte)
            btncomecar.setText('começar')
            num.setText('')
            contador = -1



contador = -1

def sortear():
    btncomecar.setText('encerrar')
    global contador
    contador += 1
    print(len(lista2))
    if len(lista2) == 0:
        criar()
    if btnSortear.text() == 'SORTEAR':
        for i in range(0,len(lista2)):
            sorteado = lista2[contador]
        num.setText(str(f'   {str(sorteado)}'))
        texto.setText(str(texto.text() + str(sorteado) + ' '))
        numSequencia.setText(texto.text())
    x = 0
    y = 440
    global v1
    print(lista2)
    for i in range(1,6):
        if i <= 1:
            for j in range(1,16):
                x = x + 52
                if j == int(num.text()):
                    v1 = QLineEdit(f'     {j} ',janela)
                    v1.setObjectName('pintar')
                    v1.setFixedSize(49,33)
                    v1.move(x,y)
                    v1.show()
            x = 0
        elif i <= 2:
            for p in range(16,31):
                x = x + 52
                if p == int(num.text()):
                    v1 = QLineEdit(f'    {p} ',janela)
                    v1.setObjectName('pintar')
                    v1.setFixedSize(49,33)
                    v1.move(x,477)
                    v1.show()
            x = 0
        elif i <= 3:
            for l in range(31,46):
                x = x + 52
                if l == int(num.text()):
                    v1 = QLineEdit(f'    {l} ',janela)
                    v1.setObjectName('pintar')
                    v1.setFixedSize(49,33)
                    v1.move(x,514)
                    v1.show()
            x = 0
        elif i <= 4:
            for a in range(46,61):
                x = x + 52
                if a == int(num.text()):
                    v1 = QLineEdit(f'    {a} ',janela)
                    v1.setObjectName('pintar')
                    v1.setFixedSize(49,33)
                    v1.move(x,551)
                    v1.show()  
            x = 0
        elif i <= 5:
            for b in range(61,76):
                x = x + 52
                if b == int(num.text()):
                    v1 = QLineEdit(f'    {b} ',janela)
                    v1.setObjectName('pintar')
                    v1.setFixedSize(49,33)
                    v1.move(x,588)
                    v1.show()    
            x = 0
    if contador >= 74:
        btnSortear.setText('RECOMEÇAR')
        
    if btnSortear.text() == 'RECOMEÇAR' and contador >= 75:
        contador = -1
        num.setText('')
        numSequencia.setText('')
        criar()
        btncomecar.setText('começar')
        btnSortear.setText('SORTEAR')
        



#botao para sortear
btnSortear = QPushButton('SORTEAR', janela)
btnSortear.setGeometry(305,740,250,40)
btnSortear.setObjectName('botaoSort')
btnSortear.clicked.connect(sortear)

btncomecar = QPushButton('começar',janela)
btncomecar.setGeometry(50,740,100,40)
btncomecar.setObjectName('botaoStart')
btncomecar.clicked.connect(criar)


num = QLineEdit('   ',janela)
num.setGeometry(370,630,130,100)
num.setObjectName('numSorteado')
#numero que foi sorteado

numSequencia = QTextEdit('   ',janela)
numSequencia.setGeometry(20,120,250,250)
numSequencia.setObjectName('numSequencia')
#numero que foi sorteado



lista1 = []
lista2 = []


#titulo
visor = QLabel('Numeros sorteados',janela)
visor.setStyleSheet('color:white; font-size: 25px;font-family:"Blippo", fantasy; font-weight: bold')
visor.setGeometry(305,337,283,100)


#roleta
roleta = QLabel('',janela)
roleta.movie = QMovie("sorteio.gif")
roleta.setMovie(roleta.movie)
roleta.movie.start()
roleta.move(330,120)



app.exec()