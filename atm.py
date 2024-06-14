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

if pin == passwrd:
    print("welcome to the ATM")
else: 
    print("Incorrect Pin") 
        