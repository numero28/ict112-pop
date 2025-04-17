import time
import sys

def NumberMismatchError(Exception):    
    pass

mobile_accounts = {
    "0244111222":{"pin": "1111","name":"Victor", "balance":100},
    "0244333444":{"pin": "3333","name":"Leo", "balance":300}
}

source_mobile_number = "0244111222"

while(True):
    time.sleep(1)
    MTN_SHORT_CODE = "*170#"
    code = input("Enter code: ")

    if code == MTN_SHORT_CODE:
        print("""
    Menu
    1) Tranfer Money
    2) MomoPay&Pay Bill
    3) Airtime&Bundles
    4) Allow Cash Out
    5) Financial Services
    6) My Wallet
    """)

        option = int(input("Enter option: "))
        
        if option == 1:
            try:
                mobile_number = input("Enter mobile number: ")
                confirmation_mobile_number = input("Confirm mobile number: ")
                
                if mobile_number == confirmation_mobile_number:
                    source_name = mobile_accounts[source_mobile_number]["name"]
                    destination_name = mobile_accounts[mobile_number]["name"]
                    source_balance = mobile_accounts[source_mobile_number]["balance"]
                    dest_balance = mobile_accounts[mobile_number]["balance"]
                    amount = float(input("Enter amount: "))
                    dest_balance = dest_balance + amount
                    source_balance = source_balance - amount
                    mobile_accounts[mobile_number]["balance"] = dest_balance
                    mobile_accounts[source_mobile_number]["balance"] = source_balance
                    fee = 0.01 * amount
                    reference = input("Enter reference: ")
                    print(f"""Transfer to {destination_name} for GHS{amount:,.2f} with reference: {reference}
    Fee is GHS {fee}. Total amount is GHS{amount:,.2f} Enter
    #for next
    _______________________

       Cancel     Send
    """)
                    
                    
                else:
                    print("Number mismatch")
                    sys.exit()
            except KeyError:
                print("Number does not exist")
        elif option == 2:
            print("""MomoPay&PayBill""")    
        elif option == 3:
            print("""Airtime&Bundles""")
        elif option == 4:
            print("""Allow Cash Out""")    
        elif option == 5:
            print("""Financial Services""")
        elif option == 6:
            print("""
My Wallet
1) Check Balance
2) Allow Cash Out
3) My Approvals
4) Report Fraud
5) Statements
6) Change&Reset PIN
7) Upgrade Profile Type
# for next
________________________

 Cancel            Send     
""")
            option = int(input("Enter option: "))
            if option == 1:
                print(f"""Fee is GHS{0:,.2f}. Enter MM PIN""")
                expected_pin = mobile_accounts[source_mobile_number]["pin"]
                entered_pin = input("Enter pin: ")                
                balance = mobile_accounts[source_mobile_number]["balance"]        
                if expected_pin == entered_pin:
                    print(f"""Current Balance:GHS{balance:,.2f}, Available
    Balance:GHS{balance:,.2f}""")
                else:
                    print("Invalid PIN")                                    
            elif option == 2:
                pass
            elif option == 3:
                pass
            elif option == 4:
                pass
            elif option == 5:
                pass
            elif option == 6:
                pass
            elif option == 7:
                print("""Next page""")
            else:
                print("Invalid option")
        else:
            print("Invalid option")
    else:
        print("""
    USS Code running....
    Connection problem or invalid MMI code
    """)