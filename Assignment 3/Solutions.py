"""
Solutions to assignment







"""
original = "Programming"def get_initials(full_name):
  
    name_parts = full_name.strip().split()
  
    initials = [name[0].upper() for name in name_parts if name]
        return '.'.join(initials) + '.'








def get_initials(full_name):
    name_parts = full_name.strip().split()
    initials = [name[0].upper() for name in name_parts if name
    return '.'.join(initials) + '.'
user_name = input("Enter your full name: ")
print("Initials:", get_initials(user_name))


def is_palindrome(s):





  
  
    s = s.replace(" ", "").lower()
    return s == s[::-1]
user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")






sentence = input("Enter a sentence:
words = sentence.split()







""
text = "This is a string and it is an example."
modified_text = text.replace("is", "was")
print(modified_text)
.
"""

