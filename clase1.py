from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication , QMainWindow,QLabel
#Application: la aplicacion en general(entorno global), Window: vista que va a vivir en la aplicacion, Label: mensaje de texto que lleva

#create the aplication
app = QApplication([])

#create the window 
window =QMainWindow()
window.setWindowTitle("My First PyQt6 Program") #titulo de la ventana 

#create the label widget
label =QLabel ("Hello, PyQt6", window) #mainwindow la que tiene todo
label.setAlignment(Qt.AlignmentFlag.AlignCenter) #quiero que el texto de la etiqueta se alinee en el centro

#Set the label as the central widget of the window
window.setCentralWidget(label)

#show the window 
window.show()

#start the application event loop
app.exec()
