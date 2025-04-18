# Assignment 3 Solutions

# 1. Reverse the string "Programming"
word = "Programming"
reversed_word = word[::-1]
print("Reversed word:", reversed_word)

# 2. Print initials in uppercase from user's full name
full_name = input("Enter your full name: ")
name_parts = full_name.strip().split()
initials = ".".join(part[0].upper() for part in name_parts) + "."
print("Initials:", initials)

# 3. Check if a string is a palindrome
text = input("Enter a word to check if it's a palindrome: ")
if text == text[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")

# 4. Count number of words in a sentence
sentence = input("Enter a sentence: ")
words = sentence.strip().split()
print("Word count:", len(words))

# 5. Replace all occurrences of "is" with "was"
text = "This is a book and it is an example."
modified_text = text.replace(" is ", " was ")
print("Modified text:", modified_text)
