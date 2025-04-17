"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
original = "Programming"
reversed_str = original[::-1]
print("Reversed using slicing:", reversed_str)



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""

def get_initials(full_name):
    # Split the full name into parts (first name, last name, etc.)
    name_parts = full_name.strip().split()
    
    # Extract the first letter of each part and capitalize it
    initials = [part[0].upper() for part in name_parts if part]
    
    # Join the initials with periods
    return '.'.join(initials) + '.'

# Get user input
user_name = input("Enter your full name: ")

# Print the initials
print("Initials:", get_initials(user_name))


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(s):
    return s == s[::-1]

# Example usage
string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome!")
else:
    print("The string is not a palindrome.")



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
def count_words(sentence):
    words = sentence.split()  # Split the sentence into words using spaces
    return len(words)

# Example usage
sentence = input("Enter a sentence: ")
word_count = count_words(sentence)
print(f"The sentence contains {word_count} words.")



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
original_string = "This is a string and it is an example."
modified_string = original_string.replace("is", "was")

print("Modified string:", modified_string)
