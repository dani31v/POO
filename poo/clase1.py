#Daniela Valencia 
print (" \n  Welcome to CFE")
print("Please add your name: ") 
name = input() 
print ("How many watts/hr you have in your bill? ") 
consumption = (float(input()))
price= 0 #por si el usuario no da un dato pues no de error

if consumption < 50:  
   price = 0
elif consumption < 100:
    price= consumption*1.1
elif consumption >=100 and consumption <200:
   price += consumption*1.2
elif consumption >=200 and consumption <300:
    price += consumption*1.3
elif consumption >=300 and consumption <400:
    price += consumption*1.4
else :
    price += consumption*1.5

print (f"{name}, you have to pay ${price}")

