
Solutions_5240101148_2025.py
Assignment 3 Solutions


# 1. Reverse the string "Programming"
original = "Programming"
reversed_str = original[::-1]
print("1. Reversed string:", reversed_str)
# Output: "gnimmargorP"


# 2. Print initials from full name
full_name = input("2. Enter your full name: ")
# Split the full name, take the first character of each part, convert to uppercase, and join with dots
initials = '.'.join([name[0].upper() for name in full_name.strip().split()]) + '.'
print("Initials:", initials)
# Example: Input: "john doe" -> Output: "J.D."


# 3. Check if a string is a palindrome
word = input("3. Enter a word to check if it's a palindrome: ")
# Compare the word with its reverse
if word == word[::-1]:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")


# 4. Count number of words in a sentence
sentence = input("4. Enter a sentence: ")
# Split the sentence into words and count
word_count = len(sentence.strip().split())
print("Number of words:", word_count)


# 5. Replace "is" with "was" in a string
text = "This is a string and it is an example."
# Replace all instances of "is" with "was"
modified_text = text.replace("is", "was")
print("5. Modified string:", modified_text)
# Output: "Thwas was a string and it was an example."
