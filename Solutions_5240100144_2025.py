"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
text = "programming"
reversed_text = text[::-1]
print(f"Reversed srting: {reversed_text} ")


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
fullName = input("Enter your full name:")
nameParts = fullName.split()
initials = '.'.join([part[0].upper()for part in nameParts])+'.'
print(f"The initials is {initials}")

"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
text = input("Enter your string:")
clean_text = text.replace("","").lower()
if clean_text==clean_text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")    


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
mySentence = input("Enter your sentence:")
words=mySentence.split()
wordCount = len(words)
print(f"Your number of words in the sentence is {wordCount}")

"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
theText = "This is a string and it is an example."
modifiedText = theText.replace("is" , "was")
print(modifiedText)