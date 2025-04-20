""" Solutions to Assignment 3 """

# 1. Reverse the string "Programming"
original_string = "Programming"
reversed_string = original_string[::-1]
print("Reversed string:", reversed_string)

# 2. Get initials in uppercase from full name
full_name = input("Enter your full name: ")
initials = ".".join([name[0].upper() for name in full_name.split()]) + "."
print("Initials:", initials)

# 3. Check if a string is a palindrome
word = input("Enter a word to check if it's a palindrome: ")
if word == word[::-1]:
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")


# 4. Count number of words in a sentence
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print("Number of words:", word_count)

# 5. Replace "is" with "was"
text = "This is a string and it is an example."
modified_text = text.replace("is", "was")
print("Modified text:", modified_text)
