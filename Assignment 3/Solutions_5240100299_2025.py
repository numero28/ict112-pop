# 1. Reverse the string "Programming"
def reverse_string(s):
    return s[::-1]  # Using string slicing to reverse the string

reversed_string = reverse_string("Programming")
print("Reversed string:", reversed_string)

# 2. Print the initials in uppercase from the user's full name
def get_initials(full_name):
    initials = ''.join([name[0].upper() + '.' for name in full_name.split()])
    return initials

user_name = input("Enter your full name: ")
print("Initials:", get_initials(user_name))



# 3. Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]  # Compare the string with its reverse

user_string = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(user_string):
    print(f'"{user_string}" is a palindrome.')
else:
    print(f'"{user_string}" is not a palindrome.')



# 4. Count the number of words in a sentence
def count_words(sentence):
    words = sentence.split()  # Split the sentence into words
    return len(words)

user_sentence = input("Enter a sentence: ")
print("Number of words:", count_words(user_sentence))


# 5. Replace all occurrences of "is" with "was"
original_string = "This is a string and it is an example."
modified_string = original_string.replace("is", "was")  # Using str.replace() to replace occurrences

print("Modified string:", modified_string)