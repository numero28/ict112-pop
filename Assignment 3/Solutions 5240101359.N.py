Here are the solutions to the assignments:
QUESTION 1
1. Reverse a string
```
string = "Programming"
reversed_string = string[::-1]
print(reversed_string)
```
QUESTIONS 2

2. Print initials in uppercase
```
full_name = input("Enter your full name: ")
initials = ".".join(name[0].upper() for name in full_name.split())
print(f"{initials}.")
```
QUESTIONS 3
3. Check if a string is a palindrome
```
string = input("Enter a string: ")
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
```
QUESTIONS 4
4. Count the number of words in a sentence
```
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print(f"The sentence contains {word_count} words.")
```
QUESTIONS 5
5. Replace "is" with "was"
```
string = "This is a string and it is an example."
modified_string = string.replace("is", "was")
print(modified_string)
```
