"""
Solutions to assignment 3
"""

# 1. Reverse the string "Programming"
original_string = "Programming"
reversed_string = original_string[::-1]
print("Reversed String:", reversed_string)

# 2. Print initials in uppercase
full_name = input("Enter your full name: ")
initials = ".".join([name[0].upper() for name in full_name.split()]) + "."
print("Initials:", initials)

# 3. Check if a string is a palindrome
text = input("Enter a string to check if it's a palindrome: ")
if text == text[::-1]:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")

# 4. Count number of words in a sentence
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print("Word Count:", word_count)

# 5. Replace all occurrences of "is" with "was"
sample_text = "This is a string and it is an example."
modified_text = sample_text.replace("is", "was")
print("Modified String:", modified_text)
