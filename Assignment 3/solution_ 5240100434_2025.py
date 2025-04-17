"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
string="Programming"
reversed_string=string[::-1]
print(f"Reversed of the String Programming is: {reversed_string}")




"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
def get_initials(full_name):
    name_parts=full_name.split()
    initials=[part[0].upper()for part in name_parts]
    return '.'.join(initials)+'.'
user_name=input("Please Enter Your full name: ")
initials=get_initials(user_name)
print(initials)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(s):
    cleaned_string = s.replace(" ", "").lower()
    return cleaned_string == cleaned_string[::-1]
user_input = input("Please enter a string: ")
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome.')
else:
    print(f"{user_input} is not a palindrome.")



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence=input("Enter a sentence: ")
words=sentence.split()
word_count=len(words)
print(f"Number of words in the sentence is:  {word_count}")



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
string="This is a string and it is an example."
modified_string=string.replace("is","was")
print(modified_string)
