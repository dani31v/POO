import typing
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication , QMainWindow,QLabel, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit

#GRID LAYOUT COLUMNAS Y FILAS COMO UNA HOJA DE EXCEL
#QVBOXLAYOUT TE ORGNIZA LOS WIDETS EN VERTICAL 
#QHBOX TE ORGANIZA LOS WIDGETS EN HORIZONTAL

class Calculator(QMainWindow):
    def __init__(self):
        super() .__init__() 
        self.setWindowTitle("Simple Calculator") #titulo de la ventana
        self.setMinimumSize(300,400) #el tamaño minimo de la ventana 
    
        #create the main widget and layout
        main_widget = QWidget(self)
        layout = QVBoxLayout(main_widget) #cada que agregue un widget dentro de otro lo va a ordenar de manera vertical
        
        #create the display QLineEdit widget
        self.display = QLineEdit() #recuadro donde insertas valores
        self.display.setReadOnly(False) #para poder editarlo el widget hay que introducir false a que solo se vea
        layout.addWidget(self.display) #este widget que acabo de crear agregaselo al layout 
        
        
        #create the buttons using a grid layout
        buttons_layout = QGridLayout()
        buttons = [
         "7", "8", "9", "/",
         "4", "5", "6", "*",
         "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]
    
        positions = [(i,j) for i in range (4) for j in range (4)] #nos da los pares ordenados para las posiciones
    
        for position, button_text in zip (positions, buttons):
         #zip crea un nuevo objeto tipo (0,0), "7", combina las listas y agrupa los pares
         button = QPushButton(button_text)#conectas un boton con el texto
         button.clicked.connect(self.button_click) #si el boton es presionado conectalo con el boton
         buttons_layout.addWidget(button, *position)#agrega al grid el boton que acabas de crear con la posicion 
         
        layout.addLayout(buttons_layout)
        self.setCentralWidget(main_widget)
        
    def button_click (self):
        button =self.sender() #quien recibio la señal
        current_text =self.display.text()
        clicked_text = button.text()
        
        if clicked_text == "=":
            try:
                result = eval (current_text)
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText("ERROR.")
        else:
            self.display.setText(current_text+clicked_text)
            
app = QApplication([])
calculator = Calculator()
calculator.show()
app.exec()