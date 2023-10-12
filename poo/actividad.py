#Print the numbers of a specified list after removing even numbers from it. 
# The program has to ask the user how many numbers he/she wants to input and 
# then perform the action.
print ("How many numbers you want to add?") #you asked to the user for the amount of numbers they want to add into the list
amountnum = int(input()) #declare integer variables
numbers = [] #declare an empty list

for n in range (0, amountnum, 1): #we use a for loop to add the numbers to the list 
    print(f"Input number #{n+1}: ") 
    c = int(input())
    if c%2 == 0: #we use a if loop in case its divisible %2 or has a reminder it'll pass
        pass #
    else:
        numbers.append(c) #if not it will add the numbers at the final of the list
    
print (f"Here is your list without even numbers:  {numbers})")

#exercise 2____________________________________________________________________________
   
# Evaluate the contents of two lists and return 
# "Both lists have at least an element in common (x)" if they have at least one common member.
# Additionally, the (x) has to be the total number of equal elements. 
# The lists can have any information.

s = [] ## we declare the lists and variables
d=[]
contador = 0

print ("How many numbers you want to add to the first list?") #you asked to the user for the amount of numbers they want to add into the list
amountnum = int(input()) #declare integer variables

for n in range (0, amountnum, 1): #we use a for loop to add the numbers to the list 
    print(f"Input number for the first list #{n+1}: ") 
    s.append(input()) #if not it will add the numbers at the final of the list

print ("How many numbers you want to add to the second list?") #you asked to the user for the amount of numbers they want to add into the list
amountnum2 = int(input()) #declare integer variables
for n in range (0, amountnum2, 1): #we use a for loop to add the numbers to the list 
    print(f"Input number for the second list #{n+1}: ") 
    d.append(input()) #if not it will add the numbers at the final of the list
    
for x in s: ## this loop will compare every item of the first list with the second one
    compare_value = x
    for i in d:
        if (compare_value == i): #and in case the elements match, the counter will add one to the sum of common elements
            contador += 1
            break
        else:
            pass
if (contador != 0):
    print(f"Both lists have at least an  element in common {contador}") ##if the counter is different of 0 it will print thw counter and message
else:
    print("There are no common elements.") ##in case the counter equals to 0 it'll print no common elements
            
#exercise 3_______________________________________________________________________________
#Obtain unique elements from two lists, inputted by the user,
# and create a third one that has the unique elements.

list3=[]
list4=[]
list5 = []
print ("How many numbers you want to add to the first list?") #you asked to the user for the amount of numbers they want to add into the list
anum3 = int(input()) #declare integer variables

for n in range (0, anum3, 1): #we use a for loop to add the numbers to the list 
    print(f"Input number for the first list #{n+1}: ") 
    list3.append(int(input()))#if not it will add the numbers at the final of the list

print ("How many numbers you want to add to the second list?") #you asked to the user for the amount of numbers they want to add into the list
anum4 = int(input()) #declare integer variables
for n in range (0, anum4, 1): #we use a for loop to add the numbers to the list 
    print(f"Input number for the second list #{n+1}: ") 
    list4.append(int(input()))#if not it will add the numbers at the final of the list



#exercise 4_______________________________________________________________________________
#Convert a list of characters into a string. The characters has to be inputted by the user.
print ("Enter the number of characters you want to convert to a string:")
characters = int(input())
listchar = []

for n in range (0, characters, 1): #we use a for loop to add the numbers to the list 
    print(f"Input character #{n+1}: ") 
    listchar.append(input())#if not it will add the numbers at the final of the list

word1 = "".join(listchar) #the method .join will let concatenate every character of the list
print(f"Your word is: {word1}")

#exercise 5_______________________________________________________________________________
#Replace the last element in a list with another list. Both lists has to be inputted by the user
print ("How many numbers you want to add to the first list?") #you asked to the user for the amount of numbers they want to add into the list
num5 = int(input()) #declare integer variables
list5_1 = []

for n in range (0, num5, 1): #we use a for loop to add the numbers to the list 
    print(f"Input number #{n+1}: for the first list") 
    list5_1.append(int(input()))#if not it will add the numbers at the final of the list

print ("How many numbers you want to add to the second list?") #you asked to the user for the amount of numbers they want to add into the list
num5_2 = int(input()) #declare integer variables
list5_2 = []

for n in range (0, num5_2, 1): #we use a for loop to add the numbers to the list 
    print(f"Input number #{n+1}: for the second list") 
    list5_2.append(int(input()))#if not it will add the numbers at the final of the list

list5_1[-1] = list5_2 #the -1 will let remove the last item and replace them with the second list
print(f"{list5_1}")



#exercise 6________________________________________________________________________________
#Move all zero digits to the end of a given list of numbers.
list6_1=[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
print (f"Numbers:{list6_1}")
for x in list6_1: ## use the for loop to compare every number in the list with the value 0
    compare_value = x
    if (compare_value == 0): ##in case one of the elements is 0 the list will add the element at the end, after remove it 
          list6_1.append(list6_1.pop(list6_1.index(0)))
          print(f"{list6_1}")
       

#exercise 7________________________________________________________________________________
#Compute average of two given lists. The lists are inputted by the user
print ("How many numbers you want to add to the first list?") #you asked to the user for the amount of numbers they want to add into the list
num7_1 = int(input()) #declare integer variables
list7_1 = [] #create an empty list
suma1 = 0
resultado = 0 #and declare the variables 

for i in range (0, num7_1, 1):
    print(f"Enter number {i+1} : ") # ask to the user to enter the numbers
    list7_1.append(int(input()))

print ("How many numbers you want to add to the second list?") #you asked to the user for the amount of numbers they want to add into the list
num7_2 = int(input()) #declare integer variables
list7_2 = []
for j in range (0, num7_2, 1):
    print(f"Enter number {j+1} : ") 
    list7_2.append(int(input()))

suma1 = sum(list7_1+list7_2) #use the process sum from the math library to sum every int of the list
resultado = suma1/len(list7_1+list7_2)  #use the function len to divide the sum between the quantity of elements
print(f"Lista 1 {list7_1}")
print(f"Lista 1 {list7_1}")
print(f"El promedio de las listas es: {resultado}") ##print the average of the lists



#exercise 8________________________________________________________________________________
#Create a program that uses only 4 lists (products, prices, stock, quantity_purchased) to create an application that perform sales. The program has the following options
#Add products
#See stock
#Create Sale
#View Sale
#Exit

#create 4 empty lists

#print the different options of the Menú
