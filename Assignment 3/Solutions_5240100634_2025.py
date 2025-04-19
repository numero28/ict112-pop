"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
value_string="Programming"
reverse_value_string=value_string[::-1]
print(reverse_value_string)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
def get_initials(name):
    parts=name().split()
    initials='.'.join(part[0].upper() for part in parts) + '.'
    return initials

full_name=input("Enter your full name: ")
print("Initials:", get_initials(full_name))


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def palindrome(string):
    string=input("Enter a string to check if palindrome: ")
    if string == string [::-1]:
        print(f"{string} is a palindrome")
        else:
            print(f"{is not a palindrome")
palindrome("level")
palindrome("radar")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence=input("Enter a sentence: ")
words=sentence split()
word_count=len(words)
print("Number of words in the sentence:", word_count)


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
text= "This is a string and it is an example."
modified_text=text.replace("is", "was")
print("Modified string:", modified_text)
