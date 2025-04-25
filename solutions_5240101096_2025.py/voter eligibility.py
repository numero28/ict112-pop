age = int(input("Enter age: "))
nationality = input("Enter nationality: ")
mental_state = input("Enter mental state: ")

if age >= 18 and nationality.upper() == "GHANAIAN" and \
   mental_state.upper() == "SOUND":
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
