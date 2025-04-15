[11/04, 22:13] Tabiri Bright: string = "Programming"
reversed_string = string[::-1]
print(reversed_string)
[11/04, 22:13] Tabiri Bright: full_name = input("Enter your full name: ")
initials = '.'.join([name[0].upper() for name in full_name.split()]) + '.'
print(initials)
[11/04, 22:13] Tabiri Bright: string = input("Enter a string: ")
if string == string[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
[11/04, 22:14] Tabiri Bright: sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words in the sentence:", len(words))
[11/04, 22:14] Tabiri Bright: string = "This is a string and it is an example."
modified_string = string.replace("is", "was")
print(modified_string)
