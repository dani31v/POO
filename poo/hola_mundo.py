print(" \n Please add a number: ")
response = int(input()) #we need to declare the type of answer we are looking for. this time we asked for enteros
print (f"Your number is {response}")
x= 9 #we declare the value of the variable
sumNumbers = response + x
print (f"The sum of the numbers are: {sumNumbers}") #it is used to only print the answer.
print(f"The sum of {response} + {x} is {sumNumbers}") #this print the numbers the user registered, the value of x and also the answer of the sum.

#mensajes con posicion

#      0123456789
msg = "Hello, I love Taylor Swift"
print (msg)
print(msg[7])
print(msg[13:22])

#mensajes con distintos tipos de letras
msg = " \n Hello, I love Taylor Swift"
print (msg.upper())
print(msg.lower())
print(msg.replace(" ","-"))

#buscar palabras o caracteres dentro de un mensaje
msg = "Hello, I love TS"
print ("TS" in msg)
print ("If" in msg)
print ("If" not in msg)

print("Username: ")
User_Name = input()
print (f"Username is: {User_Name}")