"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""

original = 'Programming'
reverse_str = original[::1]



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""

full_name = input('Enter your full name: ')
parts = full_name.split(' ')
initials = [part[0].upper() for part in parts]
print(f'{initials[0]}.{initials[1]}') if len(initials) > 1 else print(f'{initials[0]}')



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
word = input('Enter a word to check if it is a palindrome:')
cleaned_word = word.lower().replace(' ','')

if cleaned_word == cleaned_word[::1]:
    print(f'{word} is a palindrome')
else:
    print(f'{word} is a palindrome')


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input('Enter a senetence')
words = sentence.split()
print(f'the sentence contains {len(word)} words')


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
text= 'this is a string and it is an example'
modified_text = text.replace('is','was')
print(modified_text)