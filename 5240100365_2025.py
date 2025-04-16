"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
#Ans
name="programming "
print(name[::-])



"""
2.create a python program that takes a user's full name as input and prints the initials in uppercase 
Example : input: "john doe," output:"J.D."
"""
#ans
first_name=input("Enter your firstname:")
second_name=("Enter your second name:")
print(f"{first_name[0].upper()}.{second_name[0] ()})


"""
3. write a python program to check if a given string is a palindrome .A palindrome reads the same forwards
and backwards (e.g.,"radar","level")Hint: compare the string with its reverse 
"""
#ans
strg=input("Enter the word")
if strg==strg[::-1]:
print("the number is palindrome")
else:
print("the number is not palindrome")




"""
create a python program that asks the userto enter a sentence and counts  the numof words in the sentence .
Hint:use the split()method to break the the string into words.
"""
#ans
sentence =input ("Enter tbe sentence:")
w=sentence .split()
wordsen(w)
print("words in yiur sentence is,"words)



"""
5. write a python program to replace all occurrences of"is with "was"in the string"This is a string and it
is an example ."print the modified string .
"""
#ans
sentence ="this is a string and it is an example "
chan=sentence .replace ("is","was")
print(chan)
