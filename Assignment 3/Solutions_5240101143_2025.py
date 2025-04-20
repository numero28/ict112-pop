"""
Solutions to Assignment 3
Index Number: 5240101143
"""

# 1. Reverse the string "Programming"
text = "Programming"
reversed_text = text[::-1]
print("1. Reversed String:", reversed_text)

# 2. Get initials from full name input
full_name = input("\n2. Enter your full name: ").strip()
initials = '.'.join([name[0].upper() for name in full_name.split()]) + '.'
print("Initials:", initials)

# 3. Check if a string is a palindrome
word = input("\n3. Enter a word to check for palindrome: ").lower()
if word == word[::-1]:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")

# 4. Count words in a sentence
sentence = input("\n4. Enter a sentence: ")
word_count = len(sentence.split())
print("Word Count:", word_count)

# 5. Replace "is" with "was"
original_string = "This is a string and it is an example."
modified_string = original_string.replace("is", "was")
print("\n5. Modified String:", modified_string)
