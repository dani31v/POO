class Persona:
    def __init__(self, n = "", e  = 0, g ="") :
        self.nombre=  n
        self.edad = e
        self.genero= g
    
    
    def Saludo(self):
        print(f"""
        Hola, soy {self.nombre}, tengo {self.edad} y soy {self.genero}""")
        
class Alumno (Persona):
    def __init__(self, n = "", e  = 0, g ="", c = "", s = 0) :
            super ().__init__(n,e, g)
            self.camera = c
            self.smestre  =s
    
Daniela = Persona ("Daniela", 20, "F")

Daniela.Saludo()