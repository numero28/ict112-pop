import time
PASSWORD = "1234"
ATTEMPTS = 3
password_is_incorrect = True
wait_time = 10
i = 1
while (password_is_incorrect):   
    password = input("Enter password: ")
    if password == PASSWORD:
        print("Logged in successfully")
        password_is_incorrect = False
    else:
        attempts_left = ATTEMPTS - i
        if i < ATTEMPTS:
            print("Wrong password. Try again")
            print(f"You have {attempts_left} more attempt(s)")
        else:
            print(f"Logged out. Try again in {wait_time} seconds")
            time.sleep(wait_time)
            i = 0
    i = i + 1
