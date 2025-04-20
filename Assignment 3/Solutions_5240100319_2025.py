"""
Solutions to assignment 3
"""
"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
name=”programming”
Print(name[::-1])

"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
first_name = input(“Enter your first_name: “)
second_name = (“Enter your second_name: ‘)
      print(f”{first_name[0].upper()}.{second_name[0].upper()})

"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
str=input(“Enter the word: ”)
If str == str[::-1]:
        print(“the number is palindrome”)
Else:
          print(“ the number is not palindrome”)


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
Sentence=input(“Enter the sentence: “)
w=sentence.split()
words=len(w)
     print(f“words in your sentence is”, {words})

"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
sentence=”this is a string and it is an example”
chan = sentence.replace(“is”,”was”)
print(chan)
