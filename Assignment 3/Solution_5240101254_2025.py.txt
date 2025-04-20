#assignment question 1
language = 'programming'
print(language[::-1])
print('\n')

#Question 2
username = input('Enter your full name: ')
username = username.upper()
print(username)
print('\n')

#question 3
word = input('Type your in a palindrome: ')
reverse = word[::-1]

if word == word[::-1]:
    print(True)
else:
    print(False)

#Question 4
sentence = input('Type in sentence: ')
words = sentence.split()
number_of_words = len(words)
print(number_of_words)

#Question 5
string = 'This is a string and it an example'
print(string.replace(' is',' was'))

