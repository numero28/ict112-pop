"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
original="Programming"
reversed_str= original[::-1]
print(reversed_str)



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
""" 
 
full_name = input("Enter your full nameL: " )
name_parts= full_name.split() 
initials=[part[0].upper() for part in name_parts]
formatted_initials='.'. join(initials)+'.' 
print(formatted_initials)



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""


def is_palindrome(s):
   cleaned = s.replace(" "," " ).lower() 
   return cleaned == cleaned[::-1]
test_string=input("Enter a string to check for palindrome: " )
if is_palindrome(test_string):
   print(f"{test_string} is a palindrome!") 
else:
   print(f"{test_string} is not a palindrome!" )


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
""" 
sentence=input("Enter a sentence : " ) 
words= sentence.split()
word_count= len(words) 
print(f"The sentence contains {word_count} word(s).")




"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
""" 

original_string="This is a string and it is an example."
words=original_string.split()
modified_words= [ "was" if word.lower()== "is" else word for word in words ]
modified_string= "".join(modified_words)
print(modified_string)