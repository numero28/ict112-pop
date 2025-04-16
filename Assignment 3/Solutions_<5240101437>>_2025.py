"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""

#Question 1
name="programming"
name_rev=' '.join(reversed(name))
print(name_rev)

"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
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


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
#Question 3
word=input("Enter a word :")
palindrome = word[: :-1]
if word==palindrome:
      print(" This word is a palindrome ")
else:
      print("This word is not")
      
"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""

#Question 4
sentence = input("Enter a sentence: ")
outcome=sentence.split()
print(len(outcome) )

"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
#Question 5
sentence ="The boy is going home "
substitution =sentence.replace("is", "was")
print(substitution )
