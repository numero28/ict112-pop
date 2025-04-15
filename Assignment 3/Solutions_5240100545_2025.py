"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
p = 'Programming'
#reversed_p = p[::-1]
#print('Reversed string:', reversed_p )
u = ''
for r in p:
    u = r + u
print(u)



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name = input('Enter your full name: ')
name_parts = full_name.strip().split()
first_letters = ""
for i in name_parts :
    first_letters = first_letters + i[0].upper() + '.'
print(f'First letters : {first_letters}')


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
word = input('Enter word to check whether it is a palindrome:  ')
if word[::1] == word[::-1]:
    print(True)
else :
    print(False)


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input('Enter your sentence:  ')
parts = (sentence.split())
total = len(parts)
print(f'Number of individual words in the given sentence is: {total}')


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
string = 'This is a string and it is an example .'
modified = 'This {} a string and it {} an example'.format('was','was')
print(modified)



