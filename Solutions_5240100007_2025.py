#Question 1

string1 = "Programming"
reversed_string1 = string1[::-1]
print(f"The reversed string is: {reversed_string1}")

#Question 2

full_name = input("Enter your full name: ")
name_parts = full_name.split()
initials = ""
for part in name_parts:
initials += part[0].upper() + "."
print(f"The initials are: {initials}")

#Question 3

text = input("Enter a string: ")
clean_text = text.replace(" ", "").lower()
if clean_text == clean_text[::-1]:
print("The string is a palindrome.")
else:
print("The string is not a palindrome.")

#Question 4

sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = len(words)
print(f"The sentence  has {word_count} words.")

#Question 5

original_string = "This is a string and it is an example."
modified_string = original_string.replace("is", "was")
print(f"The modified string is: {modified_string}")
