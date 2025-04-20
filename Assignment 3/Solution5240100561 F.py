*Assignment 3 Solutions*
# QUESTION 1
  1. *Reverse a String*
Here's a Python program that uses string slicing to reverse the string "Programming":

```
def reverse_string(s):
    return s[::-1]

original_string = "Programming"
reversed_string = reverse_string(original_string)

print("Original String:", original_string)
print("Reversed String:", reversed_string)
```
# QUESTION 2
2. *Print Initials in Uppercase*
This Python program takes a user's full name as input and prints the initials in uppercase:

```
def print_initials(full_name):
    names = full_name.split()
    initials = ".".join(name[0].upper() for name in names)
    return f"{initials}."

full_name = input("Enter your full name: ")
print(print_initials(full_name))
```
# QUESTION 3
3. *Check if a String is a Palindrome*
Here's a Python program that checks if a given string is a palindrome:

```
def is_palindrome(s):
    s = s.lower()  # Convert to lowercase for case-insensitive comparison
    return s == s[::-1]

string = input("Enter a string: ")
if is_palindrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')
```
# QUESTION 4
4. *Count the Number of Words in a Sentence*
This Python program asks the user to enter a sentence and counts the number of words:

```
def count_words(sentence):
    words = sentence.split()
    return len(words)

sentence = input("Enter a sentence: ")
word_count = count_words(sentence)
print(f"The sentence contains {word_count} words.")
```
# QUESTION 5
5. *Replace "is" with "was" in a String*
Here's a Python program that replaces all occurrences of "is" with "was" in a given string:

```
def replace_is_with_was(s):
    return s.replace("is", "was")

original_string = "This is a string and it is an example."
modified_string = replace_is_with_was(original_string)

print("Original String:", original_string)
print("Modified String:", modified_string)
```
