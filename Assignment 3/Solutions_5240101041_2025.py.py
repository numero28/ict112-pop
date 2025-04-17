1. Reverse a String

def reverse_string(s):
    return s[::-1]

original_string = "Programming"
reversed_string = reverse_string(original_string)
print(reversed_string)


2. Get Initials from Full Name

def get_initials(full_name):
    names = full_name.split()
    initials = ".".join(name[0].upper() for name in names)
    return f"{initials}."

full_name = input("Enter your full name: ")
initials = get_initials(full_name)
print(initials)


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
    words = sentence.split()
    return len(words)

sentence = input("Enter a sentence: ")
word_count = count_words(sentence)
print(f"The sentence contains {word_count} words.")


5. Replace "is" with "was"

def replace_is_with_was(s):
    return s.replace("is", "was")

original_string = "This is a string and it is an example."
modified_string = replace_is_with_was(original_string)
print(modified_string)

