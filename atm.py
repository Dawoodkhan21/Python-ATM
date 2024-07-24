import os

def atm():
    print("Welcome to the ATM! Please Insert Your Card!!!")
    print("Please wait, while we scan your card........")

    pin = os.getenv('ATM_PIN', None)
    if not pin:
        pin = input("Enter Your 4-Digit PIN: ")
    else:
        print(f"Using provided PIN: {pin}")

    try:
        pin = int(pin)
        if len(str(pin)) != 4:
            raise ValueError("PIN must be a 4-digit number.")
    except ValueError as e:
        print(e)
        return

    print(f"PIN entered: {pin}")
    # Add more ATM logic here

if __name__ == "__main__":
    atm()
