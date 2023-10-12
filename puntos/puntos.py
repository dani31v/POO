import math
import csv

filepath = "/Users/danielavalencia/Desktop/Escritorio - MacBook Air de Daniela (2)/Carrera/segundo semestre/POO/puntos.csv"
filepath2 = "./puntos2.csv"

class Point:
    def __init__(self, x = 0.0):
        self.x = x
        self.y = 0.0
    def VerValores(self):
        print(f"({self.x}, {self.y})")
    def CalcularFuncion1(self):
        self.y =  math.exp(-abs(self.x)) * math.cos(2 * math.pi * self.x)
        

lista_puntos = []

x = 0.0
while x <= 100:
    punto_temporal = Point(x)
    punto_temporal.CalcularFuncion1()
    lista_puntos.append(punto_temporal)
    x += 0.5

# for punto in lista_puntos:
#    punto.VerValores()

file = open(filepath, 'w')   
file2 = open(filepath2, 'w')

csv_writer = csv.writer(file)
csv_writer2 = csv.writer(file2)

table_header = ['x','y']
csv_writer.writerow(table_header)
for punto in lista_puntos:
    csv_writer.writerow([punto.x, punto.y])    

file.close()

