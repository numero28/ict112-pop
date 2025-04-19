# ict112-pop Assignment 3/solutions(5240100953)-2025.py

Q1
original = "Programming"
reversed_str = original[::-1]
print("Reversed string:", reversed_str)

Q2
 full_name = input("Enter your full name: ")
initials = ".".join([name[0].upper() for name in full_name.split()]) + "."
print("Initials:", initials)

Q3
text = input("Enter a string: ")
if text == text[::-1]:
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")

Q4
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words))

Q5
original_string = "This is a string and it is an example."
modified_string=original_string.replace("is", "was")
print("Modified string:", modified_string)

