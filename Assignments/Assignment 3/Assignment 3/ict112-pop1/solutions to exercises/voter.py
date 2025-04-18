NATIONALITY = "GHANAIAN"
MENTAL_STATE = "SOUND"
LEGAL_AGE = 18

age = int(input("Enter age: "))
nationality = input("Enter nationality: ")
mental_state = input("Enter mental state: ")

if age >= LEGAL_AGE and nationality.upper() == NATIONALITY and mental_state.upper() == MENTAL_STATE:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
