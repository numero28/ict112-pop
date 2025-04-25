# List definition
fruits = ["apple", "orange", "banana"]

#printing out the list: method 1
print("Method 1")
for fruit in fruits:
    print(fruit)

print()
print("Method 2")
#printing out the list: method 2
for i in range(len(fruits)):
	print(fruits[i])
print()

#Method to calculate grade
def grade(mark):
    if mark >= 80:
        grade = "A"
    elif mark >= 75:
        grade = "B+"
    elif mark >= 70:
        grade = "B"
    elif mark >= 65:
        grade = "C+"
    elif mark >= 60:
        grade = "C"
    elif mark >= 55:
        grade = "D+"
    elif mark >= 50:
        grade = "D"
    else:
        grade = "E"
    return grade

        
"""
Write a program to compute the total and average marks obtained by 5 students.
The names, index numbers and marks are stored in three different lists. The program
calls the grade function to compute the grade obtained by each student
"""

#Names
names= ['Ama', 'Kofi', 'Abena', 'Kwame', 'Akua']
#Index numbers
index_numbers = [1111, 2222, 3333, 4444, 5555]
#Scores
marks = [78, 70, 85, 63, 69]

total = 0

print("Table of students names, index numbers, marks and grades")
print("___________________________________________________________________")
for i in range(len(names)):
    print(f"Name: {names[i]} \t| Index Number: {index_numbers[i]} \
\t| Mark: {marks[i]} \t| Grade:{grade(marks[i])}")
    print("___________________________________________________________________")

    total = total + marks[0]
average_mark = total / len(marks) 
print()
print(f"The total mark is: {total}")
print(f"The average mark is: {average_mark}")


