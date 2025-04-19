
#Solutions to assign


1#.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.

 def reverse_string(s):
    return s[::-1]
strings="programming"
print(reverse_string(strings))



2.#Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."

def get_initials(full_name):
    names = full_name.split()
    initials = [name[0].upper() for name in names]
    return '.'.join(initials) + '.'

full_name = input("Enter your full name: ")
initials = get_initials(full_name)
print("Your initials are:", initials)








3.#Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.

def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]
string1="radar"
string2="level"
print(is_palindrome(string1)) 
print(is_palindrome(string2)) 






4#.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.

sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = len(words)
print("Number of words in the sentence:", word_count)




5#Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.

original_string = "This is a string and it is an example."
modified_string = original_string.replace("is", "was")
print(modified_string)


