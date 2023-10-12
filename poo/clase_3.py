### functions and lists
# create a program that asks the user how many courses she/he is taking

### Libraries
import math

### Functions/Classes
 
def greetStudent(studentName="Student"):
    print(f"Hello {studentName}")

def askAge():
    print("How old are you? ")
    response = int(input())
    return response

def completeMessage(name,age):
    print(f"OH, that's nice {name}, you're {age} years old!")

def conversation(name):
    greetStudent(name)
    completeMessage(name, askAge())

# exercise 2 _______________________________________________________________________________
### Main
greetStudent("David")
age = askAge()
completeMessage("David", age)

conversation("David")

#              0        1         2          3
fruitList = ["apple", "banana", "cherry", "watermelon"]
myScores = [10, 9, 8.5, 7]
print(fruitList[2])
print(myScores[3])

# Create a program that asks the user how many courses
# he/she is taking, then ask for the names of the courses
# and the scores, and finally calculate the GPA
print("How many courses are you taking this semester: ")
amountCourses = int(input())
courses = []
grades = []
for course in range (0, amountCourses, 1):
    print(f"Input course #{course+1}: ")
    courses.append(input())
    print(f"What is the score of course #{course+1}: ")
    grades.append(float(input()))
GPA = 0
for index in range(0, amountCourses, 1):
    print(f"{courses[index]} - {grades[index]}")
    GPA = GPA + grades[index]
GPA = GPA/amountCourses
print(f"The GPA is : {GPA}")

#              0        1         2          3
fruitList = ["apple", "banana", "cherry", "watermelon"]
print(fruitList)
fruitList[1] = "grapes"
print(fruitList)

fruitList = ["apple", "banana", "cherry"] 
print(fruitList)
print(len(fruitList))
print("---------------")
fruitList.append("watermelon")
print(fruitList)
print(len(fruitList))
print("---------------")
fruitList.insert(2, "grape")
print(fruitList)
print(len(fruitList))
print("---------------")
fruit2 = ["coco", "mango"]
fruitList.extend(fruit2)
print(fruitList)
print(len(fruitList))
print("---------------")
numbers = [5,6,7,8,9]
fruitList.extend(numbers)
print(fruitList)
print(len(fruitList))