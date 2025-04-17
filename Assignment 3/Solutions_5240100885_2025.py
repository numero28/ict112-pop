"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
word="programming"[::-1]
print(word)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
det get_initials(full name):
name=full_name.split()
initials=".".join([name[0].under() for name in names])
return initials
full_name=input("Enter your full name:")
print(get_initials(full name))



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
i=input("Enter any word")
reversed_i=i[::-1]
if i==reversed_i:
else:    
    print("palindrom")




"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence=input("Enter any sentence:")
word=sentence.spilt()
word_count=len(word)
print("Number of word:",word_count)



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""text="This is a string and it is an examples"
new_text=text.replace("is","was")
print(new_text)