#Grading system
name = input("Enter name: ")
score = float(input("Enter score: "))

if score <0 or score >100:
    print("Score should be between 0 and 100")    
else:
    if score >= 80:
        grade = "A"
    elif score >= 75:
        grade = "B+"
    else:
        grade = "C"
    print(f"Name: {name}\nScore: {score}\nGrade: {grade}")
