class Car:
    def __init__(self, cp = "", m = "", b = "", y = 0, p = 0.0):
        self.carPlate = cp
        self.model = m
        self.brand = b
        self.year = y
        self.price = p
        
    def printCarData(self):
        print (f"{self.carPlate}- {self.brand} {self.model} {self.year}")
        print (f"Price: ${self.price}")
        
class Company:
    def __init__(self, cn = ""):
        self.name = cn
        self.carList = []
    def add_car(self, car):
       #amount = input ("How many cars of this model do you") (examen)
        self.carList.append(car)
    def show_car_list(self):
        for car in self.carList:
            car.printCarData()
            print()
    def show_specific_carData(self, CarP  =""):
        for car in self.carList:
            if car.carPlate == CarP:
                car.printCarData ()
                break
            else:
                print ("Car Plate not found")
    def delete_car(self, CarP  =""):
        for index in range ( 0, len(self.carList),1):
            if self.carList[index].carPlate == CarP:
                self.carList.pop(index)
                break
            else:
                print ("Car Plate not found")
   