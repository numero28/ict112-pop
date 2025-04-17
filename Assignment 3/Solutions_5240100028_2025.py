

### 1. Reverse the string "Programming"
original_string = "Programming"
reversed_string = original_string[::-1]
print(reversed_string)


### 2. Print initials from a full name
full_name = input("Enter your full name: ")
parts = full_name.split()
initials = [part[0].upper() for part in parts]
print(f"{initials[0]}.{initials[1]}." if len(initials) > 1 else f"{initials[0]}.")


### 3. Check if a string is a palindrome
string = input("Enter a string to check for palindrome: ")
if string == string[::-1]:
    print(f"'{string}' is a palindrome")
else:
    print(f"'{string}' is not a palindrome")


### 4. Count words in a sentence
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print(f"The sentence contains {word_count} words.")


### 5. Replace "is" with "was"
original_text = "This is a string and it is an example."
modified_text = original_text.replace("is", "was")
print(modified_text)


