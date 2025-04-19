"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
data="Programming"
reverse_data=data[::-1]
print(reverse_data)

"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name=input("Enter full name:")
name_list=full_name.split()
initials=[parts[0].upper() for part in name_list:]
name_initials= '.'.join(initials)
print(name_initials)

"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
myword=input('Enter a word')
reverse_myword=myword[::-1]
if reverse_myword.lower()==myword.lower():
  print('The word is palindrome')
else:
  print('The word is not palindrome')

"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
statement=input('Enter a sentence:')
num_statement=statement.split()
count=len(num_statement):
print(f'There are {count} words in the sentence.')
  
"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
statement='The dog is cute, it is always neat.'
final=statement.replace('is', 'was')
print(final)
