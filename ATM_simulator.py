# ATM Simulator - Mini Project (Beginner Level)

correct_pin = "1234"
balance = 5000.0


def check_balance(balance):
    print(f"Aapka current balance hai: {balance}")


def deposit(balance):
    amount = float(input("Kitna deposit karna hai? "))
    if amount > 0:
        balance = balance + amount
        print(f"{amount} deposit ho gaya. Naya balance: {balance}")
    else:
        print("Invalid amount!")
    return balance


def withdraw(balance):
    amount = float(input("Kitna withdraw karna hai? "))
    if amount <= 0:
        print("Invalid amount!")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance = balance - amount
        print(f"{amount} withdraw ho gaya. Naya balance: {balance}")
    return balance


def atm():
    global balance
    pin = input("Apna PIN enter karo: ")

    if pin != correct_pin:
        print("Galat PIN! Access Denied.")
        return

    print("PIN sahi hai. Welcome!")

    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Apna choice enter karo (1-4): ")

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            print("Dhanyawad! ATM band ho raha hai.")
            break
        else:
            print("Invalid choice, dubara try karo.")


# Program start
atm()