"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
def reverse_string_slicing(s):
    return s[::-1]
original_string = "programming"
reversed_string = reverse_string_slicing(original_string)
print("reversed string:",reversed_string)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
userfullname = input("enter name full name:")
split_name = userfullname.split()
initials = " ".join(firstletter[0].upper() for firstletter in split_name)+"."
print(initials)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
word = input("enter word:")
reversalword = word[::-1]
if word == reversalword:
    print("it is a palindrome")
else:
    print("it is not a palindrome")    



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input("enter a sentence:")
split_sentence = sentence.split()
split_words = len(split_sentence)

print(f"the number of words in the sentence is {split_words}")



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
text = "This is a sting and it is an example."

replaced = text.replace("is","was")
print(replaced)