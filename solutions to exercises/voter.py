NATIONALITY = "TOGOLESE"
MENTAL_STATE = "sound"
LEGAL_AGE = 18

age = int(input("Enter age: "))
nationality = input("Enter nationality: ")
mental_state = input("Enter mental state: ")

if age>=18 and nationality.upper()==NATIONALITY and
mental_state==MENTAL_STATE:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
