"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
original string="programming"
reversed_string=original_string[::-1]
print(reversed string)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
full name = input("enter your full name")
name parts = full name.split( )
initials = [part [0].upper( ) for part in name parts]
initials_str = "".join(initials)
print(initials_ste)




"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
def is_palindrome(s):
    # Remove spaces and convert to lowercase for a case-insensitive comparison
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

# Example usage
input_str = input("Enter a string: ")
if is_palindrome(input_str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
def count_words(sentence):
    # Split the sentence into words based on whitespace
    words = sentence.split()
    return len(words)

# Get input from the user
user_input = input("Enter a sentence: ")

# Count the words and display the result
word_count = count_words(user_input)
print("Number of words in the sentence:", word_count)



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.

# Original string
text = "This is a string and it is an example."

# Replace 'is' as a whole word with 'was'
modified_text = re.sub(r'\bis\b', 'was', text)

# Print the modified string
print("Modified string:", modified_text)
