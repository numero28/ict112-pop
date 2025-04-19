*solutions to all five questions* in your Assignment 3:

```python
Solutions to Assignment 3
Index Number: 5240101345
Year: 2025

1.original_string = "Programming"
reversed_string = original_string[::-1]
print(reversed_string)



2.full_name =  input("Enter your full name:")
initials = full_name[0].upper() + "." + full_name[7].upper()
print(initials)



3.def is_palindrome(string):
 	return string == string[::-1]
input_string = input("Enter a string:")
if is_palindrome(input_string):
	print(f"{input_string} is a palindrome.")
else:
	print(f"{input_string} is not a palindrome.")



4.sentence = input("Enter a sentence:")
word_count = len(sentence.split())
print(f"The sentence has {word_count} words.")


5.original_string = "This is a string and it is an example."
modified_string = original_string.replace("is", "was")
print(modified_string)