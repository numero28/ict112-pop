"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""name="programming"
print(name[::-1])




"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""first_name=input("Enter your firstname: ")
second_name=("Enter your secondname: ")
print(f"{first_name[0].upper()}.{second_name[0].upper()})




"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""strg = input("Enter a word: ")
if strg == strg[::-1]:  # Reversing the string to check palindrome condition
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")





"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""sentence = input("Enter a sentence: ")
words = sentence.split()  # Splitting the sentence into words
word_count = len(words)  # Counting the words
print("The number of words in your sentence is:", word_count)






"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""sentence="this is a string and it is an example"
chan=sentence.replace("is","was")
print(chan)
