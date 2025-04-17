"""
Solutions to assignment 3
"""

# 1. Reverse the string "Programming"
original = "Programming"
reversed_string = original[::-1]
print("1. Reversed string:", reversed_string)

# 2. Get initials from full name
full_name = input("2. Enter your full name: ")
initials = ".".join([name[0].upper() for name in full_name.split()]) + "."
print("Initials:", initials)

# 3. Check if a string is a palindrome
text = input("3. Enter a string to check for palindrome: ")
is_palindrome = text == text[::-1]
print("Is palindrome:", is_palindrome)

# 4. Count number of words in a sentence
sentence = input("4. Enter a sentence: ")
word_count = len(sentence.split())
print("Number of words:", word_count)

# 5. Replace all "is" with "was"
sample_text = "This is a string and it is an example."
modified_text = sample_text.replace("is", "was")
print("5. Modified string:", modified_text)
