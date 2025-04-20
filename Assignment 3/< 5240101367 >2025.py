"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
str="programming"
str1="programming"
for i in str:
str1 = i+str1
print(str1)

"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
my string= input("john doe:")
print("JOHN DOE")
print(john doe.upper())


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def check(st):
    rev=st[::-1]
    print("string  : ",st)
    print("Reverse : ",rev)
    if(st==rev):
        return True
    else:
        return False
x=input("radar","level:")
if check(x):
      print("it is a palindrome")
else:
    print("it is not a palindrome")
    


"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
string = input('Enter a sentence: ')
str1 = string.split(' ')
str1s = set(str1)
str1s = list(str1s)
str1s.sort()
counter = []
for i in str1s:
    counter.append(str1.count(i))
for i in range(len(str1s)):
    print(str1s[i], ':',counter[i])
    


"""
5.Write a to" Print the modified string.
"""
st = input(":" )
old_st = input(":" )
new_st =input(":" )
x = st.replace(old_st, new_st)
print(x)
y = st.replace(old_st, new_st, 1)
print(y)
z = st.replace(old_st, new_st, 2)
print(z)
