# ATM Simulator - Mini Project (with Easy Additions)

correct_pin = "1234"
balance = 5000.0
transaction_history = []   # NEW: list to store all transactions
wrong_pin_attempts = 0      # NEW: track wrong PIN tries


def check_balance(balance):
    print(f"Aapka current balance hai: {balance}")


def deposit(balance):
    amount = float(input("Kitna deposit karna hai? "))
    if amount > 0:
        balance = balance + amount
        transaction_history.append(f"Deposit: +{amount}")   # NEW
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
        transaction_history.append(f"Withdraw: -{amount}")   # NEW
        print(f"{amount} withdraw ho gaya. Naya balance: {balance}")
    return balance


def view_history():   # NEW function
    if len(transaction_history) == 0:
        print("Koi transaction nahi hui abhi tak.")
    else:
        print("----- Transaction History -----")
        for transaction in transaction_history:
            print(transaction)


def change_pin():   # NEW function
    global correct_pin
    old_pin = input("Purana PIN enter karo: ")
    if old_pin != correct_pin:
        print("Purana PIN galat hai!")
        return
    new_pin = input("Naya PIN enter karo: ")
    correct_pin = new_pin
    print("PIN successfully change ho gaya!")


def atm():
    global balance, wrong_pin_attempts

    while wrong_pin_attempts < 3:   # NEW: limit check
        pin = input("Apna PIN enter karo: ")

        if pin == correct_pin:
            wrong_pin_attempts = 0   # reset on success
            break
        else:
            wrong_pin_attempts += 1
            remaining = 3 - wrong_pin_attempts
            if remaining > 0:
                print(f"Galat PIN! {remaining} attempt(s) bache hain.")
            else:
                print("Account locked! Bahut zyada galat attempts.")
                return

    print("PIN sahi hai. Welcome!")

    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Transaction History")
        print("5. Change PIN")
        print("6. Exit")

        choice = input("Apna choice enter karo (1-6): ")

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            view_history()
        elif choice == "5":
            change_pin()
        elif choice == "6":
            print("Dhanyawad! ATM band ho raha hai.")
            break
        else:
            print("Invalid choice, dubara try karo.")


# Program start
atm()