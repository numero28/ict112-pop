
#Solutions to assignment 3



#1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.

string ="programming"
reversed_string =string[::-1]
print(reversed_string)


#.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."

def_initials(full_name)
names=full_name.split()
initials =""
for name in names:
    initials +=name[0].upper()="."
return initials
full_name=input("Enter your full name: ")
print("initials:"get_initials(full_name))


#.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.

def is_palindrome(text):
    text =text.lower()

return text==text[::-1]
string =input("Enter a string:")
if is_palindrome(string):
    print(f"'{string}'is a palindrome.")
    else:
         print(f"'{string}'is not a palindrome.")




4#.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.


def count_vowels(sentence):
    vowels ="aeiouaeiou"
    vowel_count = 0
    for char in sentence:
        if char in vowels:
            vowels_count+=1
            return vowels_count
            sentence=input("Enter a sentence")
            num_vowels =count_vowels(sentence)
            prin("number of vowels:"num_vowels)


5#.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.

sentence ="this is an example."
nodified_sentence= sentence .replace("is","was")
print(modified_sentence)