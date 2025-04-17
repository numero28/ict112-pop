"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
string ="Programming"
reversed_string =string[::-1]
print(reversed_string)

"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name = input("Enter your full name:")
initials=[]
for i in full_name:
    if i.isupper():
        initials.append(i)
print(initials[0] + "." + initials[1])

"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""

string=input("Enter a string:")
processed_string=''.join(ch for ch in string.lower()if ch.isalnum())
if processed_string==processed_string[::-1]:
 print("The string is a palindrome.")
else:
 print("The string is not a palindrome.")

"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence=input("Enter a sentence:")
words=sentence.spilt()
print("Number of words:",len(words))


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
string="This is a string and it is an example."
modified_string=string.replace("is","was")
print(modified_string)