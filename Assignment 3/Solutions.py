"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
Define the input string
input_string = "Programming"

 Use string slicing to reverse the string
reversed_string = input_string[::-1]

 Print the reversed string
print(reversed_string)



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
Take user input for full name
full_name = input("Enter your full name: ")

Split the full name into first and last names
first_name, last_name = full_name.split()

 Get the first letter of each name
first_initial = first_name[0]
last_initial = last_name[0]

 Print the initials in uppercase
print(f"{first_initial}.{last_initial}.")



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
Define a function to check if a string is a palindrome
def is_palindrome(string):
     Reverse the string
    reversed_string = string[::-1]

     Check if the original string is equal to the reversed string
    if string == reversed_string:
        return True
    else:
        return False

 Take user input for the string to check
input_string = input("Enter a string: ")

 Call the function and print the result
if is_palindrome(input_string):
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome.")



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
Take user input for the sentence
sentence = input("Enter a sentence: ")

 Use the split() method to break the sentence into words
words = sentence.split()

 Print the number of words in the sentence
print(f"The sentence has {len(words)} words.")


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
Define the input string
input_string = "This is a string and it is an example."

 Replace all occurrences of "is" with "was"
modified_string = input_string.replace("is", "was")

 Print the modified string
print(modified_string)
