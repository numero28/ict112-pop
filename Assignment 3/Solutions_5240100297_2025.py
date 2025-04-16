
# 1. Reverse the string "Programming"
word = "Programming"
reversed_word = word[::-1]  # Using string slicing to reverse
print("Reversed string:", reversed_word)


# 2. Get initials in uppercase from user's full name
full_name = input("Enter your full name: ")  # Example input: "john doe"
names = full_name.strip().split()  # Split the name into parts
initials = ".".join([name[0].upper() for name in names]) + "."
print("Initials:", initials)



# 3. Check if a string is a palindrome
text = input("Enter a word to check if it's a palindrome: ")  # Example: "radar"
if text == text[::-1]:  # Compare with its reverse
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")



# 4. Count the number of words in a sentence
sentence = input("Enter a sentence: ")  # Example: "This is a test sentence."
words = sentence.strip().split()  # Split sentence into words
print("Number of words:", len(words))



# 5. Replace all "is" with "was" in a given string
text = "This is a string and it is an example."
modified_text = text.replace("is", "was")
print("Modified string:", modified_text)
