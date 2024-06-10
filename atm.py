import time

balance = 5000
transaction_records = [] 

print("Welcome to the ATM! Please Insert Your Card!!!")
time.sleep(1)
print("Please wait, while we scan your card...", end='', flush=True)
for _ in range(5):
    print(".", end='', flush=True)
    time.sleep(1)
print()
passwrd = 3214
pin = int(input("Enter Your 4-Digit PIN: "))

while True:
    if pin == passwrd:
        print("""
              How can I help you!!!
              
              1: Balance
              2: Withdraw
              3: Deposit
              4: Transfer
              5: Transaction Record
              6: Quit
              """)
        try:
            option = int(input("Choose Your Option: "))
        except ValueError:
            print("Please Enter a Valid Input")

        if option == 1:
                print("Please wait...", end='', flush=True)
                for _ in range(5):
                    print(".", end='', flush=True)
                    time.sleep(1)
                print()
                print("Your Current Balance is:", balance, "PKR")
        elif option == 2:
            withdraw = int(input("Enter the amount you want to withdraw: "))
            if withdraw <= balance:
                balance -= withdraw
                print("Please wait...", end='', flush=True)
                for _ in range(5):
                    print(".", end='', flush=True)
                    time.sleep(1)
                print()
                print(f"""{withdraw} PKR has been successfully withdrawn from your account.
                      Your updated balance is: {balance} PKR.""")
                transaction_records.append({'type': 'Withdrawal', 'amount': withdraw})
            else: 
                print("Insufficient balance!!!")
        elif option == 3:
            deposit = int(input("Enter the amount you want to deposit: "))
            balance += deposit
            print("Please wait...", end='', flush=True)
            for _ in range(5):
                print(".", end='', flush=True)
                time.sleep(1)
            print()
            print(f"""{deposit} PKR has been successfully deposited to your account.
                  Your updated balance is: {balance} PKR.""")
            transaction_records.append({'type': 'Deposit', 'amount': deposit})
        elif option == 4:
            while True:
                accname = input("Enter the Receiver Name: ")
                accno = int(input("Enter the Receiver Account no: "))
                transfer = int(input(f"Enter the amount to be transferred to {accname}: "))
                print("Please wait...", end='', flush=True)
                for _ in range(5):
                    print(".", end='', flush=True)
                    time.sleep(1)
                print()
                print(f"""
                      Please Verify Receiver Details
                      Account Holder Name: {accname}
                      Account Number: {accno}
                      Amount to be Transferred: {transfer} PKR
                      """)
                verify = input("Are these details correct? (Y/N): ")
                if verify.lower() == 'y':
                    if transfer <= balance:
                        balance -= transfer
                        transaction_records.append({'type': 'Transfer', 'amount': transfer})

                        print(f"{transfer} PKR transferred to {accname}. Your updated balance is: {balance} PKR")
                    else:
                        print("Insufficient balance!!!")
                    break  
                elif verify.lower() == 'n':
                    print("Transaction canceled!!! Please re-enter receiver details.")
                else:
                    print("Invalid input. Please enter 'Y' or 'N'.")
        elif option == 5:
            print("Transaction Records:")
            for record in transaction_records:
                print(f"{record['type']} - {record['amount']} PKR")
            print(f"Current Balance is {balance} PKR")
        elif option == 6:
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid option. Please choose a valid option.")
