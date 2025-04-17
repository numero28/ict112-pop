#1. Reverse string

text = "Programming"
reversed_text = text[::-1]  # Using string slicing
print(reversed_text)

#2. extracting initials from full name

name = input("Enter full name: ")
initials = ".".join([word[0].upper() for word in name.split()])
print(initials + ".")

#3. Check if a given string is palindrome

text = input("Enter a string: ")
if text == text[::-1]:  
    print("Palindrome")
else:
    print("Not a palindrome")

#4. Count words in sentence

sentence = input("Enter a sentence: ")
word_count = len(sentence.split())  
print("Word count:", word_count)

#5. Replace "is" with "was"

text = "Programming is fun but it is too difficult."
modified_text = text.replace("is", "was")
print(modified_text)
