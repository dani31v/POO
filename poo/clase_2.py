import math as m #This is the library "math" with the name "m"
print("\n Enter point x1:") #Ask for a point and add the input for the user enter the data
x1= float(input())

#this process is repeated 4 times to obtain all the points
print("Enter point y1:")
y1= float(input())


print("Enter point x2:")
x2= float(input())


print("Enter point y2:")
y2= float(input())


# declare variables that had a formula to find the middle point in x as well as the points in y
mx=(x1+x2)/2
my=(y1+y2)/2

#now we print the result
print(f"The middle point is ({mx},{my}) ") 

#exercise 2_____________________________________________

#we ask for a number to be the variable x
print("Enter the value of x: ")
x= float(input())

#This formula with the math library and the value of x solve this problem
formula = m.pow(m.e,-(m.fabs(x))) * m.cos(2 * m.pi * x)
# print the solution 
print (f"The solution for the formula is: {formula}")

