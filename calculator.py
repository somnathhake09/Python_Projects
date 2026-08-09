def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
def show_menu():
    print("\n----- Calculator Menu -----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
            print(f"The result of addition is: {addition(num1, num2)}")
        elif choice == '2':
            print(f"The result of subtraction is: {subtraction(num1, num2)}")
        elif choice == '3':
            print(f"The result of multiplication is: {multiplication(num1, num2)}")     
        elif choice == '4':
            try:
                print(f"The result of division is: {division(num1, num2)}")         
            except ValueError as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()
