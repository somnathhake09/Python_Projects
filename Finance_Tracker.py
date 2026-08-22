print("=" * 40)
print("Personal Finance Tracker")
print("=" * 40)

income_str = input("Enter Your Monthly Income:")
income = float(income_str)
transactions =[]

while True:
    descriptiopn = input("\nEnter Expense Description (or 'done' to Finish): ")
    if descriptiopn.strip().lower() == "done":
        break

    amount_str = input("Enter Amount:")
    amount =float(amount_str)

    category = input("Enter category (Food/Rent/Travel/Other): ")

    if category.strip().lower() in ("food", "rent"):
        spend_type ="Essential"
    elif category.strip().lower() in ("travel" , "entertainment"):
        spend_type = "discretionary"
    else:
        spend_type = "Unknown"

    transactions.append(descriptiopn,amount,category,spend_type)
    print(f"Added : {descriptiopn} - {amount:.2f} ({spend_type})")


print("\n" + "=" * 40)
print("All Transactions")
print("=" * 40)

total_spent = 0
for t in transactions:
    desc, amt, cat, spend_type = t
    print(f"{desc:<15} {amt:>10.2f} [{cat} - {spend_type}]")
    total_spent += amt 

remaining_balance =income - total_spent
spent_percentage = (total_spent / income) * 100 if income > 0 else 0

print("\n" + "=" *( 40))
print("Monthly Summary")
print("=" * 40)
print(f"Total transactions : {len(transactions)}")
print(f"Total_spent        : {total_spent:.2f}")
print(f"Monthly Income     : {income:.2f}")
print(f"% of Income Spent  : {spent_percentage:.2f}%")
print(f"Remaining Balance  : {remaining_balance:.2f}")

if total_spent > income:
    print("\n ⚠️ You are OVERSPENDING this Month !")
elif spent_percentage > 80 :
    print("\n ⚠️ You're Close to your income limit -- be careful. ")
else:
    print("\n ✅ You're within a healthy spending range. ")