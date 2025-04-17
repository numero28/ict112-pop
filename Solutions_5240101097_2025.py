"""
Solutions to Assignment 3
Name: Osei Emmanuel Gyabaah
Index Number: 5240101097
"""

# 1. Reverse the string "Programming"
s = "Programming"
reversed_s = s[::-1]
print("1. Reversed string:", reversed_s)

# 2. Take the user's full name (pre‑filled) and print the initials in uppercase
full_name = "Osei Emmanuel Gyabaah"
initials = [part[0].upper() for part in full_name.split() if part]
print("2. Initials:", ".".join(initials) + ".")

# 3. Check if a given string is a palindrome
text = input("3. Enter a string to check for palindrome: ")
clean = text.replace(" ", "").lower()
if clean == clean[::-1]:
    print(f'   "{text}" is a palindrome.')
else:
    print(f'   "{text}" is not a palindrome.')

# 4. Count the number of words in an entered sentence
sentence = input("4. Enter a sentence: ")
word_count = len(sentence.split())
print("   Number of words in the sentence:", word_count)

# 5. Replace all occurrences of "is" with "was" in the given string
original = "This is a string and it is an example."
modified = original.replace("is", "was")
print("5. Modified string:", modified)
