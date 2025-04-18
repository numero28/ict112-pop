"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
x="programming"
reversed_x = x[::-1]
print(reversed_s)

"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name = input(" Enter your full name: ").strip()
names = full_name.split()
initials = ".".join(name[0].upper() for name in names) + "."
print("   Initials:", initials)


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
word = input("3. Enter a string to check for palindrome: ").strip()
if word == word[::-1]:
    print(f"   '{word}' is a palindrome.")
else:
    print(f"   '{word}' is not a palindrome.")


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input("4. Enter a sentence: ").strip()
word_count = len(sentence.split())
print("   Number of words:", word_count)

"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""original = "This is a string and it is an example."
modified = original.replace("is", "was")
print(modified)
"""



