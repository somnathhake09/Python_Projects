contacts ={}
{"Somnath": "9876543210", "Rahul": "9123456789"}

def add_contact():
    name = input("Naav taak: ")
    number = input("Phone number taak: ")
    contacts[name] = number
    print(f"{name} add zala contacts madhe!")

def view_contacts():
    if len(contacts) == 0:
        print("Ajun koni contact nahi aahe!")
    else:
        print("--- Contact List ---")
        for name, number in contacts.items():
            print(f"{name}: {number}")

def search_contact():
    name = input("Konta naav search karaycha? ")
    if name in contacts:
        print(f"{name} cha number: {contacts[name]}")
    else:
        print(f"{name} sapadla nahi contacts madhe!")

def delete_contact():
    name = input("Konta contact delete karaycha? ")
    if name in contacts:
        del contacts[name]
        print(f"{name} delete zala!")
    else:
        print(f"{name} sapadla nahi, delete karta yenar nahi!")

def main():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Kay karaycha aahe? (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Contact Book band karतोय. Bye!")
            break
        else:
            print("Chukіcha choice, punha try kar!")

main()
