#Question 1
name="programming"
name_rev=' '.join(reversed(name))
print(name_rev)


#Question 2
# Get full name from the user
full_name = input("Enter your full name: ")

# Split the name into parts (first, middle, last, etc.)
name_parts = full_name.strip().split()

# Extract the first letter of each part and capitalize it
initials = [part[0].upper() for part in name_parts]

# Join the initials with dots
formatted_initials = ".".join(initials) + "."

# Print the result
print("Initials:", formatted_initials)


#Question 3
word=input("Enter a word :")
palindrome = word[: :-1]
if word==palindrome:
      print(" This word is palindrome ")
else:
      print("It is not")
      
#Question 4
sentence = input("Enter a sentence: ")
outcome=sentence.split()
print(len(outcome) )

#Question 5
sentence ="The boy is my friend "
Replace =sentence.replace("is", "was")
print(Replace )
