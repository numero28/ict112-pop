# 1. Reverse the string "Programming"
string1 = "Programming"
reversed_string1 = string1[::-1]
print(f"The reversed string of '{string1}' is: {reversed_string1}")

# 2. Get initials from a full name
full_name = input("Enter your full name: ")
name_parts = full_name.split()
initials = ""
for part in name_parts:
    initials += part[0].upper() + "."
print(f"The initials are: {initials[:-1]}") # Remove the trailing dot

# 3. Check if a string is a palindrome
string2 = input("Enter a string to check for palindrome: ")
string2 = string2.lower() # Ignore case
reversed_string2 = string2[::-1]
if string2 == reversed_string2:
    print(f"'{string2}' is a palindrome.")
else:
    print(f"'{string2}' is not a palindrome.")

# 4. Count the number of words in a sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = len(words)
print(f"The sentence has {word_count} words.")

# 5. Replace "is" with "was" in a string
string3 = "This is a string and it is an example."
modified_string = string3.replace("is", "was")
print(f"The modified string is: {modified_string}")
