# from Classes import Car --- only imports one class
# from Classes import Car, Company
import classes as c #this imports all the classes 

def print_menu():
    print (""" 
           1.- Add Car
           2.- Show Car List
           3.- Show Specific 
           4.- Delete Car in List
           5.- Exit
           """)

def add_car(Company):
    temporal_car= c.Car() #this create a temporal car
    temporal_car.carPlate = input("Input the car plate: ")
    temporal_car.brand = input("Input the car brand: ")
    temporal_car.model = input("Input the car model: ")
    temporal_car.year = int(input("Input the car year: "))
    temporal_car.price = float(input("Input the car price: "))
    Company.add_car(temporal_car)
    return Company #this is for update the class


myCompany = c.Company("UP Cars")
program_running = True

while program_running:
    print_menu()
    option = int (input("Select an option: "))
    if option  == 1:
        myCompany= add_car(myCompany)
    elif option == 2:
        myCompany.show_car_list()
    elif option == 3:
        CarP = input("Input car plate: ")
        myCompany.show_specific_carData(CarP)
    elif option == 4:
        CarP = input("Input car plate: ")
        myCompany.delete_car(CarP)
    elif option == 5:
        print ("Closing the program")
        program_running = False
    else: 
        print("Option not valid")