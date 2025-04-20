"""
LISTS are ordered and mutable
"""

#Defining a list of fruits
fruits = ["Orange", "Apple", "Kiwi"]

#Printing out each fruit in the list
for fruit in fruits:
    print(fruit)

#Adding a new fruit to the list 
fruits.append("Guava")

#Printing the fruit list to view the new addition
for fruit in fruits:
    print(fruit)

#printing out each fruit item using their index
for i in range(len(fruits)):
    print(fruits[i])

#Defining a list of ages of people
ages = [18, 19, 21, 20]

#Printing out each age in the list
for age in ages:
    print(age)

#A list of course codes
course_codes = ["ICT112", "ICT111", "MAT119",
           "ICT113", "EDC111", "ACC111",
           "GPD111"]
#Changing the list item in index 2 to MAT113
course_codes[2] = "MAT113"
print(course_codes)

"""
TUPLES are ordered and immutable
"""

#The tuple of colours making up the AAMUSTED logo 
aamusted_colors = ("Wine", "Green", "Yellow")

#Printing out each colour
for aamusted_color in aamusted_colors:
    print(aamusted_color)

#Tuples are unmutable so the following code will generate an error
#aamusted_colors[2] = "Blue"

"""
SETS are unordered, are mutable and contain unique values. Set operations
such s difference, union and intersection can be applied on them
"""

#A set of odd numbers 
odd_numbers = {1, 3, 5, 7, 7}

#a set of even numbers
even_numbers = {2, 4, 6, 8}

#Printing out the odd numbers one by one
for odd_number in odd_numbers:
    print(odd_number)

#Set operations
intersection = odd_numbers & even_numbers
union = odd_numbers | even_numbers
difference = odd_numbers - even_numbers

print(f"Intersection: {intersection}")
print(f"Union: {union}")
print(f"Difference: {difference}")

"""
Dictionaries are ordered and mutable. They contain key, value pairs
"""

#A dictionary containing a student's details
student = {
    "index_number": 5211040111,
    "name" : "Delani",
    "age": 19,
    "gender" : "male",
    "programme": "BSc ITE"
    }

#Printing out the key value pair of the student details
for key, value in student.items():
    print(f"{key} -> {value}")
    
#A dictionary containing details of 3 students    
students = {
           5211040111: {"name" : "Delani",
           "age": 19,
           "gender" : "male",
           "programme": "BSc ITE"},

           5211040112 : {"name" : "Alice",          
           "age": 18,
           "gender" : "female",
           "programme": "BSc ITE"},

           5211040113:{"name" : "Bob",
           "age": 23,
           "gender" : "male",
           "programme": "BSc ITE"}
            }
    
#Printing out the details of each student
for key, value in students.items():
    print(f"{key} : {value}")

#Printing out individual details of a student 
print(student["name"])
print(student["programme"])
    
# A dictionary of products
products = {
1:{'item': "milk","unit_price":15, "qty":200},
2:{'item': "sugar","unit_price":20, "qty":150},
3:{'item': "honey","unit_price":7, "qty":20}
}

#Computing the total product sales
grand_total = 0

for key, value in products.items():    
    total = (products[key]["unit_price"] * products[key]["qty"])
    print(f"{products[key]['item']} : {total}")
    grand_total = grand_total + total
    
average = grand_total / len(products)
print(f"Grand total: {grand_total}")
print(f"{Average: {average}}")