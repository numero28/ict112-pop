"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""

# 1
word = "programming"
word_decrement = 1
wordlenght = len(word)
capsiding_word =""
for i in word:
    last_word= word[wordlenght - word_decrement]
    capsiding_word += last_word
    
    word_decrement +=1
    
print(capsiding_word)
print(word[::-1])

# 2

full_name = input("Enter your full name: ")

name_parts = full_name.split()

initials = ".".join(part[0].upper() for part in name_parts) + "."
print(initials)

#3
text = input("Enter a string: ")
cleaned_text = text.replace(" ", "").lower()
if cleaned_text == cleaned_text[::-1]:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
    
    
# 4
sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = len(words)
print("Number of words in the sentence:", word_count)

#5
text = "This is a string and it is an example."
replacement = text.replace("is", "was")
print(replacement)