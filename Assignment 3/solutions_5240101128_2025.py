"""
Solutions to assignment 3
"""

# 1. Reverse the string "Programming"
word = "Programming"
reversed_word = word[::-1]
print("Reversed string:", reversed_word)


# 2. Print initials from full name
full_name = input("Enter your full name: ")
initials = ".".join([name[0].upper() for name in full_name.split()]) + "."
print("Initials:", initials)


# 3. Check if a string is a palindrome
text = input("Enter a word to check if it's a palindrome: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


# 4. Count number of words in a sentence
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print("Number of words:", word_count)


# 5. Replace "is" with "was"
original_string = "This is a string and it is an example."
modified_string = original_string.replace("is", "was")
print("Modified string:", modified_string)
