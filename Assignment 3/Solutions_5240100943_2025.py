
# 1. Reverse the string "Programming"
original_string = "Programming"
reversed_string = original_string[::-1]
print("Reversed String:", reversed_string)

# 2. Get initials from full name
full_name = input("Enter your full name: ")
initials = ".".join([name[0].upper() for name in full_name.split()]) + "."
print("Initials:", initials)

# 3. Check if a string is a palindrome
word = input("Enter a word: ")
if word == word[::-1]:
    print(f'"{word}" is a palindrome.')
else:
    print(f'"{word}" is not a palindrome.')


# 4. Count number of words in a sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words))

# 5. Replace "is" with "was" in the given string
text = "This is a string and it is an example."
modified_text = text.replace("is", "was")
print("Modified String:", modified_text)
