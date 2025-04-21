*solutions to all five questions* in your Assignment 3:

```python
Solutions to Assignment 3
Index Number: 5240101448
Year: 2025

1. Reverse the string "Programming"
text = "Programming"
reversed_text = text[::-1]
print("1. Reversed string:", reversed_text)

2. Print initials in uppercase from full name
full_name = input("\n2. Enter your full name: ")
initials = ".".join([name[0].upper() for name in full_name.strip().split()]) + "."
print("Initials:", initials)

3. Check if a string is a palindrome
word = input("\n3. Enter a word to check if it's a palindrome: ")
is_palindrome = word == word[::-1]
print("Is palindrome:", is_palindrome)

4. Count number of words in a sentence
sentence = input("\n4. Enter a sentence: ")
word_count = len(sentence.strip().split())
print("Word count:", word_count)

5. Replace "is" with "was" in a given sentence
original = "This is a string and it is an example."
modified = original.replace("is", "was")
print("\n5. Modified string:", modified)
```

---