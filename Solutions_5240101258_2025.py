"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
def reverse_string(s):
  return s[::-1]

string = "Programming"
reversed_string = reverse_string(string)
print(reversed_string)

"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""

def get_initials(full_name):
    return ".".join(s[0].upper() for s in full_name.split()) if full_name else ""

if __name__ == "__main__":
    name = input("Enter your full name: ").strip()
    if name:
        print("Initials:", get_initials(name))
    else:
        print("No input.")
        
"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(text):
  cleaned_text = ''.join(char.lower() for char in text if char.isalnum()) #remove non-alphanumeric and lowercase
  return cleaned_text == cleaned_text[::-1] #compare cleaned string to reversed cleaned string.

user_input = input("Enter a string: ")

if is_palindrome(user_input):
  print(f"'{user_input}' is a palindrome.")
else:
  print(f"'{user_input}' is not a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words
"""
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print("Word count:", word_count)


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""

print("This", "is a string and it is an example.".replace("is", "was")) 
