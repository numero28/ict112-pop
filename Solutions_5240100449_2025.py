"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""

Text="programming"
Text_to_be_reversed=Text[::-1]
print(f"Your reversed text:{Text_to_be_reversed}")


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name=input("Enter full name:")
Part_name=full_name.strip().split()
initials=""
for part in Part_name:
    if part:
        initials+=part[0].upper()+"."
print(initials)



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""

word="madam"
word_lower_case=word.lower()
if word_lower_case==word_lower_case[::-1]:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")
    print(word_lower_case[::-1])


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""

sentence=input("Type a sentence:")
sentence1=sentence.split()
print(f"Number of words in your sentence is:{len(sentence1)}")


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
Text="He is a boy and he is cute"
Text_to_be_replace=Text.replace("is","was")
print(f"Your new sentence is:{Text_to_be_replace}")
