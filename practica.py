from PyQt6.QtWidgets import QApplication
from models import *
from utilscopy import*
import sys

def main():
    app = QApplication(sys.argv)#investiga que es sys.argv
    
    window = MainWindow()#declaramos la ventana como variable/ventana principal
    window.show()# le damos un atributo a la ventana que es mostrarla
    
    app.exec() #ejecutamos la app