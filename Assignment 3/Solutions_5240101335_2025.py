"""
Solutions to assignment 3
"""

# 1. Reverse the string "Programming"
original = "Programming"
reversed_str = original[::-1]
print("Reversed string:", reversed_str)

# 2. Get initials in uppercase from user's full name
full_name = input("Enter your full name: ")
initials = ".".join([name[0].upper() for name in full_name.split()]) + "."
print("Initials:", initials)

# 3. Check if a string is a palindrome
string = input("Enter a word to check if it's a palindrome: ")
if string == string[::-1]:
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")

# 4. Count the number of words in a sentence
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print("Number of words in the sentence:", word_count)

# 5. Replace all occurrences of "is" with "was"
text = "This is a string and it is an example."
modified_text = text.replace("is", "was")
print("Modified string:", modified_text)
