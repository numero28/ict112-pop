"""
Solutions to assignment 3
"""

"""

"""
SOLUTION 1
original_string = "Programming"
reversed_string = original_string[::-1]
print("Reversed string:", reversed_string)



"""

""
SOLUTION 2
full_name = input("Enter your full name: ")
name_parts = full_name.strip().split()
initials = ""
for part in name_parts:

    initials += part[0].upper() + "."
print("Initials:", initials)



"""

"""
SOLUTION 3
text = input("Enter a string to check if it's a palindrome: ")
cleaned_text = text.replace(" ", "").lower()
reversed_text = cleaned_text[::-1]
if cleaned_text == reversed_text:
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")



"""
"""
SOLUTION 4
sentence = input("Enter a sentence: ")
words = sentence.strip().split()
word_count = len(words)
print("Number of words in the sentence:", word_count)



"""
""


SOLUTION 5
  text = "This is a string and it is an example."
modified_text = text.replace("is", "was")
print("Modified string:", modified_text)
