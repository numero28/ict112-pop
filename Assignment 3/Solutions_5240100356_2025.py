"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
#Reversing the string using slicing
reversed_str="programming"[::-1]
print(reversed_str)




"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
#Get input,split into parts,and format initials
full_name=input("Enter your full name").strip()
names=full_name.split()


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
#compare the string with its reverse
string=input("Enter a string").strip()
if string ==string[::-1]:
    print("Not a palindrome")
else
    print("it's not a palindrome")

4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
#split the sequence into words and count them 
sentence = input("Enter a sentence:").strip()
word_count= len(sentence.split())

print(f"Number of words:{word_count})")
"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string."

"""
#Replace all occurrence of "is" with "was"
original= "This is a string and it is an example."
modified= original.replace("is","was")