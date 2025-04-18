
Here are the solutions to the assignment:
#QUESTION 1
Solution 1: Reverse a String
```
def reverse_string(s):
    return s[::-1]

string = "Programming"
reversed_string = reverse_string(string)
print(reversed_string)
```
QUESTION 2
Solution 2: Print Initials in Uppercase
```
def print_initials(full_name):
    names = full_name.split()
    initials = ".".join(name[0].upper() for name in names)
    return f"{initials}."

full_name = input("Enter your full name: ")
print(print_initials(full_name))
```
#QUESTION 3
Solution 3: Check if a String is a Palindrome
```
def is_palindrome(s):
    return s == s[::-1]

string = input("Enter a string: ")
if is_palindrome(string.lower()):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
```
#QUESTION 4
Solution 4: Count the Number of Words in a Sentence
```
def count_words(sentence):
    return len(sentence.split())

sentence = input("Enter a sentence: ")
word_count = count_words(sentence)
print(f"The sentence contains {word_count} words.")
```
#QUESTION 5 
Solution 5: Replace "is" with "was" in a String
```
def replace_string(s):
    return s.replace("is", "was")

string = "This is a string and it is an example."
modified_string = replace_string(string)
print(modified_string)
```
