"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
worrd="programming"
[::-1]
print(word)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
def 
get_initials(full_name):
    names = full_name.split()
    intials = ".".join([name[0].up per() for name in names])
    return initials full_name = input("Enter your full name: ")
print(get_initials(full_name))


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
i = input("Enter any word")
reversed_i = i[::-1]
if i == reversed_i:
    print("palindrome")
else:
    print("None-palindrome")

"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input("Enter any sentence: ")
word = sentence.split()
wolrd_count = len(word)
print("Number olf word:",word_count)


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
new_text = text.replace("is","was")
print(new_text)