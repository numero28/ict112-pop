"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""

mainWord = "Programming"

theReverseWord =mainWord[::-1]

print("the Reverse String: ",theReverseWord)



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""

fullName = input("Enter your full name: ")

groupName = fullName.split()

initialName = ".".join(firstletter[0].upper() for firstletter in groupName) +"."


print(initialName)





"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""

word = input("Enter a word: ")

reverseWord = word[::-1]

if word == reverseWord:
    print("it's a palindrome")
else:
    print("it's not a palindrome")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""

sentence = input("Enter a sentence: ")

sentenceSplit = sentence.split()

wordSplit = len(sentenceSplit)


print("The number of words in the sentence is ", wordSplit)


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""

sentence = "This is a string and it is an example"

replaceWord = sentence.replace("is","was")


print("modified string: ", replaceWord)


        
