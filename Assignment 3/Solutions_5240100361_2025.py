"""
Solutions to assignment 3
"""
"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
text = "Programming"
reversed_text = text[::-1]
print("The Reverse string: ",reversed_text)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name = input("Enter your full name: ")
name_part = full_name.split()
inital_name = ",".join(first_letter[o] for first_letter in name_part
print(first_name)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
text= input("Enter a string: ")
text = text.lower()
if text == text:[::-1]:
print(f"{text} is a palindrome)
else:
print(f"{text} is not a palindrome)

"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input("Enter a sentence: ")
words = sentence.split
word_count = len(word)
print(f"Number of words in a sentence: ",word_count)

"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
  text = "This is string and it is an an example"
replace_word = sentence.replace("is","was")
print("Modified String: ",replace_word)
