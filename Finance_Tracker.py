
import json
from pathlib import Path

DATA_FILE = Path("transactions.json")


def load_transactions(filename=DATA_FILE):
    if not filename.exists():
        return []

    try:
        with open(filename, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # file exists but has invalid/empty JSON — start fresh instead of crashing
        print("Warning: data file was empty or corrupted. Starting fresh.")
        return []


def save_transactions(transactions, filename=DATA_FILE):
    with open(filename, "w") as f:
        json.dump(transactions, f, indent=2)


def get_transaction():
    description = input("\nEnter expense description (or 'done' to finish): ").strip()
    if description.lower() == "done":
        return None

    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Rent/Travel/Other): ").strip().title()
    spend_type = classify_expense(category)

    return {
        "description": description,
        "amount": amount,
        "category": category,
        "spend_type": spend_type,
    }


def classify_expense(category, essential_list=("Food", "Rent")):
    if category in essential_list:
        return "Essential"
    elif category in ("Travel", "Entertainment"):
        return "Discretionary"
    else:
        return "Unknown"


def calculate_totals(transactions):
    total_spent = 0
    category_totals = {}
    for t in transactions:
        total_spent += t["amount"]
        cat = t["category"]
        category_totals[cat] = category_totals.get(cat, 0) + t["amount"]
    return total_spent, category_totals


def find_highest_category(category_totals):
    if not category_totals:
        return None, 0
    highest_category = max(category_totals, key=category_totals.get)
    return highest_category, category_totals[highest_category]


def calculate_remaining(income, total_spent):
    return income - total_spent


def calculate_percentage_spent(income, total_spent):
    if income == 0:
        return 0
    return (total_spent / income) * 100


def print_transaction_list(transactions):
    print("\n" + "=" * 40)
    print("ALL TRANSACTIONS (including previously saved)")
    print("=" * 40)
    for t in transactions:
        print(f"{t['description']:<15} {t['amount']:>10.2f}  [{t['category']} - {t['spend_type']}]")


def print_summary(income, total_spent, remaining, percent_spent):
    print("\n" + "=" * 40)
    print("MONTHLY SUMMARY")
    print("=" * 40)
    print(f"Total spent         : {total_spent:.2f}")
    print(f"Monthly income      : {income:.2f}")
    print(f"% of income spent   : {percent_spent:.2f}%")
    print(f"Remaining balance   : {remaining:.2f}")

    if total_spent > income:
        print("\n⚠️  You are OVERSPENDING this month!")
    elif percent_spent > 80:
        print("\n⚠️  You're close to your income limit — be careful.")
    else:
        print("\n✅ You're within a healthy spending range.")


def print_category_breakdown(category_totals, highest_category, highest_amount):
    print("\n" + "=" * 40)
    print("SPENDING BY CATEGORY")
    print("=" * 40)
    for cat, total in category_totals.items():
        print(f"{cat:<15}: {total:.2f}")

    if highest_category:
        print(f"\nHighest spending category: {highest_category} ({highest_amount:.2f})")

    unique_categories = set(category_totals.keys())
    print(f"You spent across {len(unique_categories)} unique categories: {unique_categories}")


def main():
    print("=" * 40)
    print("PERSONAL FINANCE TRACKER - v4")
    print("=" * 40)
    transactions = load_transactions()
    if transactions:
        print(f"Loaded {len(transactions)} previously saved transaction(s).")
    else:
        print("No previous data found — starting fresh.")

    income = float(input("Enter your monthly income: "))
    
    while True:
        transaction = get_transaction()
        if transaction is None:
            break
        transactions.append(transaction)
        print(f"Added: {transaction['description']} - {transaction['amount']:.2f} "
            f"({transaction['spend_type']})")
    save_transactions(transactions)
    print(f"\n💾 Saved {len(transactions)} total transaction(s) to {DATA_FILE}")

    total_spent, category_totals = calculate_totals(transactions)
    remaining = calculate_remaining(income, total_spent)
    percent_spent = calculate_percentage_spent(income, total_spent)
    highest_category, highest_amount = find_highest_category(category_totals)

    print_transaction_list(transactions)
    print_summary(income, total_spent, remaining, percent_spent)
    print_category_breakdown(category_totals, highest_category, highest_amount)

if __name__ == "__main__":
    main()