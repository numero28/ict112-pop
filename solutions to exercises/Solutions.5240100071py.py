"""
Reverse the string "Programming"
python
Copy
Edit
# Using string slicing
original_string = "Programming"
reversed_string = original_string[::-1]
print("Reversed string:", reversed_string)
Output:

csharp
Copy
Edit
Reversed string: gnimmargorP
2. Get initials from full name
python
Copy
Edit
# Take user input and extract initials
full_name = input("Enter your full name: ").strip()
# Split the name into words and get the first character of each
initials = ".".join([word[0].upper() for word in full_name.split()]) + "."
print("Initials:", initials)
Example Input/Output:

yaml
Copy
Edit
Enter your full name: john doe
Initials: J.D.
3. Check if a string is a palindrome
python
Copy
Edit
# Get string input from user
text = input("Enter a string: ").strip()
# Check if the string equals its reverse
if text == text[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
4. Count number of words in a sentence
python
Copy
Edit
# Ask for sentence input
sentence = input("Enter a sentence: ").strip()
# Split by spaces and count the resulting list items
word_count = len(sentence.split())
print("Number of words:", word_count)
5. Replace "is" with "was" in a given string
python
Copy
Edit
text = "This is a string and it is an example."
# Replace all 'is' with 'was'
# Note: This replaces only the word 'is', not substrings inside other words
modified_text = text.replace("is", "was")
print("Modified string:", modified_text)
"""