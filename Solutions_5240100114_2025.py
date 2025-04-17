# Solutions_5240100114_2025.py

# 1. Reverse the string "Programming"
string = "Programming"
print("Reversed string:", string[::-1])
print()

# 2. Get initials in uppercase
full_name = input("Enter your full name:\n")
initials = ".".join([word[0].upper() for word in full_name.split()]) + "."
print("Initials:", initials)
print()

# 3. Palindrome checker
def is_palindrome(s):
    return s == s[::-1]
word = input("Enter a word:\n")
if is_palindrome(word):
    print(f'"{word}" is a palindrome.')
else:
    print(f'"{word}" is not a palindrome.')
print()

# 4. Word count in a sentence
sentence = input("Enter a sentence:\n")
print("Word count:", len(sentence.split()))
print()

# 5. Replace "is" with "was"
text = "Thís is a string and it is an example."
print("Modified string:", text.replace("is", "was"))
