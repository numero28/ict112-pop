1. Reverse a String

def reverse_string(s):
    return s[::-1]

string = "Programming"
print(reverse_string(string))  # Output: "gnimmargorp"


2. Print Initials in Uppercase

def print_initials(full_name):
    initials = ".".join(name[0].upper() for name in full_name.split())
    return f"{initials}."

full_name = input("Enter your full name: ")
print(print_initials(full_name))


3. Check if a String is a Palindrome

def is_palindrome(s):
    return s == s[::-1]

string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


4. Count Words in a Sentence

def count_words(sentence):
    return len(sentence.split())

sentence = input("Enter a sentence: ")
print(f"The sentence contains {count_words(sentence)} words.")


5. Replace "is" with "was"

def replace_is_with_was(s):
    return s.replace("is", "was")

string = "This is a string and it is an example."
print(replace_is_with_was(string))

