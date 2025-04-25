#Simulation of a bank app
import sys

PIN = 1234
balance = 10250

while(True):
    print("""
    ==================================
      WELCOME TO THE ICT112 BANK APP  
    ==================================
    """)

    my_pin = int(input("\tEnter PIN:"))

    if my_pin == PIN:

        print("""
    ==================================
      WELCOME TO THE ICT112 BANK APP 
    ==================================
    *                                *
    * 1 - Withdraw                   *
    * 2 - Deposit                    *
    * 3 - Check Balance              *
    * 4 - Quit                       *
    *                                *
    **********************************
        """)
        
        option = int(input("\tEnter option: "))
        if option == 1:
            print(f"\tYour balance is: {balance:.2f} ")
            amount = float(input("\tEnter amount to withdraw: "))
            balance = balance - amount
            print(f"\tYour new balance is: {balance:.2f} ")
        elif option == 2:
            print(f"\tYour balance is: {balance} ")
            amount = float(input("\tEnter amount to deposit: "))
            balance = balance + amount
            print(f"\tYour new balance is: {balance:.2f} ")
        elif option == 3:
            print(f"\tYour balance is: GHS{balance:,.2f} ")

        else:
            sys.exit()        

    else:
        print("\tIncorrect PIN")
