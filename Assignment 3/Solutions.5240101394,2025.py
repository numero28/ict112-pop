#Quetion 1
string1 = "I love programming"
print(string1.startswith("I"))
print(string1.endswith("love"))

#Quetion 2
string = "Programming"
reversed_string = string[::-1]
print(f"reversed string: {reversed_string}")

#Quetion 3
text = input("Enter a string: ")
if text == text[::-1]:
    print("It's a palindrome")
else:
    print("It's not a palindrome")

#Quetion 4
sentence = input("Enter a sentence: ")
words = sentence.split()
print(f"Number of words: {len(words)}")

#Quetion 5
string = ("This is what is expected from you")
modified_string = string.replace("is", "was")
print(modified_string)
