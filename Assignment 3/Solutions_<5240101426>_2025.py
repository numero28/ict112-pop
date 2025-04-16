Q1. Define the string
text = "Programming"
reversed_text = text[::-1]
print(reversed_text)

Q2. full_name = input("Enter your full name: ")
name_parts = full_name.split()
initials = "".join([part[0].upper() for part in name_parts])

 Print the initials in the desired format
print(".".join(initials) + ".")


Q3. string = input("Enter a string: ")
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.)

Q4. Get the sentence from the user
sentence = input("Enter a sentence: ")
words = sentence.split()

 Print the number of words
print("Number of words in the sentence:", len(words))

Q5. Replace 'is' with 'was'
modified_text = text.replace(" is ", " was ")

 Print the modified string
print(modified_text)
