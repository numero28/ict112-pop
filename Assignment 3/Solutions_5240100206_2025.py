
#Solutions to assignment 3

# 1. Reverse the string "Programming"
print("1. Reverse the string 'Programming'")
text = "Programming"
reversed_text = text[::-1]
print("Reversed string:", reversed_text)
print()  # For spacing

# 2. Print initials in uppercase
print("2. Print initials in uppercase")
full_name = input("Enter your full name: ")
initials = ".".join([name[0].upper() for name in full_name.split()]) + "."
print("Initials:", initials)
print()

# 3. Check if a string is a palindrome
print("3. Check if a string is a palindrome")
text = input("Enter a string: ")
if text == text[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
print()

# 4. Count number of words in a sentence
print("4. Count number of words in a sentence")
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words))
print()

# 5. Replace all 'is' with 'was'
print("5. Replace all 'is' with 'was'")
text = "This is a string and it is an example."
modified_text = text.replace("is", "was")
print("Modified string:", modified_text)
