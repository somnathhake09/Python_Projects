"""
Mini Project: Daily Expense Analyzer
Concept Used: Lambda Functions with map(), filter(), reduce()

This project analyzes a person's daily expenses using functional
programming concepts instead of traditional loops.
"""

from functools import reduce

# ------------------- Sample Data -------------------
# Each expense is a dictionary: category, amount, date
expenses = [
    {"category": "Food", "amount": 250, "date": "2026-08-01"},
    {"category": "Travel", "amount": 100, "date": "2026-08-02"},
    {"category": "Shopping", "amount": 1200, "date": "2026-08-03"},
    {"category": "Food", "amount": 180, "date": "2026-08-04"},
    {"category": "Entertainment", "amount": 500, "date": "2026-08-05"},
    {"category": "Travel", "amount": 60, "date": "2026-08-06"},
    {"category": "Food", "amount": 320, "date": "2026-08-07"},
    {"category": "Bills", "amount": 1500, "date": "2026-08-08"},
]


# ------------------- Core Functions using Lambda -------------------

def get_total_expense(expense_list):
    """Use reduce() with lambda to sum all amounts"""
    return reduce(lambda total, item: total + item["amount"], expense_list, 0)


def filter_by_category(expense_list, category):
    """Use filter() with lambda to get expenses of a specific category"""
    return list(filter(lambda item: item["category"] == category, expense_list))


def filter_above_amount(expense_list, limit):
    """Use filter() with lambda to get expenses above a certain amount"""
    return list(filter(lambda item: item["amount"] > limit, expense_list))


def apply_discount(expense_list, percent):
    """Use map() with lambda to apply a discount/cashback on every expense"""
    return list(map(
        lambda item: {**item, "amount": round(item["amount"] * (1 - percent / 100), 2)},
        expense_list
    ))


def get_category_names(expense_list):
    """Use map() with lambda to extract just category names, then remove duplicates"""
    return list(set(map(lambda item: item["category"], expense_list)))


def sort_by_amount(expense_list, descending=True):
    """Use sorted() with lambda as the key function"""
    return sorted(expense_list, key=lambda item: item["amount"], reverse=descending)


def category_wise_total(expense_list):
    """Combine filter + reduce with lambda to get total per category"""
    categories = get_category_names(expense_list)
    result = {}
    for cat in categories:
        cat_expenses = filter_by_category(expense_list, cat)
        result[cat] = reduce(lambda total, item: total + item["amount"], cat_expenses, 0)
    return result


# ------------------- Menu Driven Program -------------------

def display_expenses(expense_list):
    if not expense_list:
        print("No expenses found.")
        return
    print(f"{'Category':<15}{'Amount':<10}{'Date':<12}")
    print("-" * 37)
    for item in expense_list:
        print(f"{item['category']:<15}{item['amount']:<10}{item['date']:<12}")


def main():
    while True:
        print("\n----- Daily Expense Analyzer -----")
        print("1. Show All Expenses")
        print("2. Show Total Expense (reduce)")
        print("3. Filter by Category (filter)")
        print("4. Filter Expenses Above Amount (filter)")
        print("5. Apply Discount/Cashback on All (map)")
        print("6. Show All Unique Categories (map)")
        print("7. Sort Expenses by Amount (sorted + lambda)")
        print("8. Category-wise Total (filter + reduce)")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_expenses(expenses)

        elif choice == "2":
            total = get_total_expense(expenses)
            print(f"Total Expense: ₹{total}")

        elif choice == "3":
            cat = input("Enter category (Food/Travel/Shopping/Entertainment/Bills): ")
            result = filter_by_category(expenses, cat)
            display_expenses(result)

        elif choice == "4":
            limit = float(input("Enter amount limit: "))
            result = filter_above_amount(expenses, limit)
            display_expenses(result)

        elif choice == "5":
            percent = float(input("Enter discount percentage: "))
            result = apply_discount(expenses, percent)
            display_expenses(result)

        elif choice == "6":
            categories = get_category_names(expenses)
            print("Unique Categories:", categories)

        elif choice == "7":
            result = sort_by_amount(expenses)
            display_expenses(result)

        elif choice == "8":
            result = category_wise_total(expenses)
            print("\nCategory-wise Total:")
            for cat, total in result.items():
                print(f"{cat}: ₹{total}")

        elif choice == "9":
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()