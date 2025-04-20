"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
# Defining the string
givenString = "programming"

# Reverse the string using string slicing
reversedString = givenString[::-1]

# Print the reversed string
print("Reversed string:", reversedString)



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
def get_initials(fullName):
    # Split the full name into a list of names
    nameParts = fullName.split()
    
    # Extract the first letter of each name part and convert it to uppercase
    initials = [name[0].upper() for name in nameParts]
    
    # Join the initials into a single string
    initials_str = ''.join(initials)
    
    return initials_str

# Get the user's full name as input
user_full_name = input("Please enter your full name: ")

# Get the initials and print them
initials = get_initials(user_full_name)
print("Your initials are:", initials)



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(s):
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the cleaned string reads the same forwards and backwards
    return cleaned_string == cleaned_string[::-1]

# Example usage
test_strings = ["radar", "level", "hello", "A man, a plan, a canal, Panama"]
for string in test_strings:
    if is_palindrome(string):
        print(f'"{string}" is a palindrome.')
    else:
        print(f'"{string}" is not a palindrome.')



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
def count_words(sentence):
    words = sentence.split()
    return len(words)

def main():
    sentence = input("Please enter a sentence: ")
    word_count = count_words(sentence)
    print(f"The number of words in the sentence is: {word_count}")

if __name__ == "__main__":
    main()



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
originalString = "This is a string and it is an example"

# Replace all occurrences of 'is' with 'was'
modifiedString = originalString.replace("is", "was")

# Printing the modified string
print(modifiedString)
