Here are the solutions:
# QUESTION 1
1. Reverse a string
```
def reverse_string(s):
    return s[::-1]

string = "Programming"
print(reverse_string(string))  # Output: "gnimmargorp"
```
# QUESTION 2
2. Print initials in uppercase
```
def print_initials(full_name):
    initials = [name[0].upper() for name in full_name.split()]
    return ".".join(initials) + "."

full_name = input("Enter your full name: ")
print(print_initials(full_name))
```
# QUESTION 3
3. Check if a string is a palindrome
```
def is_palindrome(s):
    return s == s[::-1]

string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
```
# QUESTION 4
4. Count the number of words in a sentence
```
def count_words(sentence):
    return len(sentence.split())

sentence = input("Enter a sentence: ")
print(f"The sentence contains {count_words(sentence)} words.")
```
# QUESTION 5
5. Replace "is" with "was"
```
def replace_is_with_was(s):
    return s.replace("is", "was")

string = "This is a string and it is an example."
print(replace_is_with_was(string))
```
