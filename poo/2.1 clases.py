
# class Product:
#     def __init__(self, id = 0, name= "", iva =False):
#         self.id = id
#         self.name = name
#         self.has_iva = iva
#     def change_id(self, id):
#         self.id = id
#     def change_name (self,name):
#         self.name = name
#     def change_iva (self,iva):
#         self.has_iva = iva
  
# myproduct = Product()
# myproduct2 = Product(15,"Aspirina",True)

# print(f"Product 1 name : {myproduct.name}")
# print(f"Product 2 name : {myproduct2.name}")

# myproduct.change_name("Redoxon")

# print(f"Product 1 name (updated): {myproduct.name}")
# print(f"Product 2 name : {myproduct2.name}")


class point2D:
    def __init__(self, x =0, y = 0):
        self.x  =x 
        self.y = y
    def printvalues(self):
        print(f"({self.x}, {self.y})")
        
point1= point2D()
point2= point2D(2,2)
point3 = point2D(point1.x + point2.x, point1.y +point2.y)

x = input("Input value x: ")
y = input("Input value y: ")
point4 = point2D(x,y)

print(f"({point1})")
point1.printvalues()
print(f"({point1.x}, {point1.y})")

#-------------------------------------------------------------------------------------
product = {
    "ID": 0,
    "Name" : "",
    "HasIva": False
}

# Encapsulation
# Abstraction
# Inheritance
# Polymorphism

# A class within a classs
# class Presentation:
#     def __init__(self):
#         self.units = ""

# class Product:
#     def __init__(self):
#         self.id = 0
#         self.name = ""
#         self.has_iva = False
#         self.presentation = Presentation()


# Definition of functions in a class vs global functions
# def change_name_product(p, name):
#     p.name = name

# class Product:
#     def __init__(self, id = 0, name = "", iva = False):
#         self.id = id
#         self.name = name
#         self.has_iva = iva
#     def change_id(self, id):
#         self.id = id
#     def change_name(self, name):
#         self.name = name
#     def change_iva(self, iva):
#         self.has_iva = iva
    

# myProduct = Product()
# myProduct2 = Product(15,"Aspirina",True)

# print(f"Product 1 name: {myProduct.name}")
# print(f"Product 2 name:{myProduct2.name}")

# myProduct.change_name("Redoxon")

# print(f"Product 1 name (updated): {myProduct.name}")
# print(f"Product 2 name: {myProduct2.name}")

class point2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def print_values(self):
        print(f"({self.x},{self.y})")
    def print_x(self):
        print(f"x: {self.x}")
    def print_y(self):
        print(f"y: {self.x}")
    def add_values(self, x_value, y_yalue):
        self.x += x_value
        self.y += y_yalue
    def add_values_from_point(self, point):
            self.x += point.x
            self.y += point.y
    def define_values_user(self):
        self.x = input("Input value x: ")
        self.y = input("Input value y: ")
        
point1 = point2D()    # 0, 0
point2 = point2D(2,2) # 2, 2
point3 = point2D(point1.x + point2.x, point1.y + point2.y)

point1.print_values()
point1.add_values(1, 1)
point1.print_values()
point1.add_values_from_point(point2)
point1.print_values()

# x = input("Input value x: ")
# y = input("Input value y: ")
# point4 = point2D(x, y)

# print(f"({point1})")
# print(f"({point1.x}, {point1.y})")
# point1.x += 5
# point1.y += 6