#   Question 1
word="progrmming"

reversed_word=word[::-1]
print(reversed_word)

#   Question 2
My_name=input("Please enter your full name: ")
starting_Letters=".".join([name[0].upper() for name in My_name.split()])
print("Initials:",starting_Letters)

#   Question 3

text=input("Please enter the letter: ")
if starting_Letters==starting_Letters[::-1]:
    print(f"{starting_Letters} is palindrome")
else:
    print(f"{starting_Letters} is not a palindrome")

#   Question 4

Words=input("Please provide a sentence here: ")
sentence_count=len(Words.split())
print(f"The words in the sentence is {sentence_count}")

#   Question 5

main_string="This is the string amd it is an example."
modified_string=main_string.replace("is","was")
print(f"The new string is:  {modified_string}")
