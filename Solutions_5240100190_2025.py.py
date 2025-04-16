"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""

# Original string
original_string = "Programming"

# Reversing 
reversed_string = original_string[::-1]


print("Reversed string:", reversed_string)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
def get_initials(full_name):
    """Return the initials of a full name in uppercase."""
    names = full_name.split()
    initials = ".".join(name[0].upper() for name in names)
    return f"{initials}."

def main():
    full_name = input("Enter your full name: ")
    initials = get_initials(full_name)
    print(initials)

if __name__ == "__main__":
    main()




"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(s):
    # Remove spaces and convert to lowercase for a case-insensitive comparison
    cleaned = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return cleaned == cleaned[::-1]

# Get user input
text = input("Enter a string: ")

# Check and display result
if is_palindrome(text):
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""

sentence = input("Enter a sentence: ")
# Split the sentence into words using split()
words = sentence.split()
word_count = len(words)
print("Number of words in the sentence:", word_count)



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
# Original string
text = "This is a string and it is an example."

# Replace all occurrences of "is" with "was"
modified_text = text.replace("is", "was")

print("Modified string:",modified_text)
