class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def update_stock(self, amount):
        self.quantity += amount

    def display_info(self):
        print(f"ID: {self.product_id} | Name: {self.name} | Price: ₹{self.price} | Qty: {self.quantity} | Total Value: ₹{self.total_value()}")


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, price, quantity):
        if product_id in self.products:
            print("Product ID already exists! Use 'restock' to update stock.")
        else:
            self.products[product_id] = Product(product_id, name, price, quantity)
            print(f"'{name}' added to inventory.")

    def remove_product(self, product_id):
        if product_id in self.products:
            removed = self.products.pop(product_id)
            print(f"'{removed.name}' removed from inventory.")
        else:
            print("Product ID not found.")

    def restock_product(self, product_id, amount):
        if product_id in self.products:
            self.products[product_id].update_stock(amount)
            print(f"Stock updated. New quantity: {self.products[product_id].quantity}")
        else:
            print("Product ID not found.")

    def sell_product(self, product_id, amount):
        if product_id not in self.products:
            print("Product ID not found.")
            return
        product = self.products[product_id]
        if product.quantity < amount:
            print(f"Not enough stock! Available: {product.quantity}")
        else:
            product.update_stock(-amount)
            print(f"Sold {amount} '{product.name}'. Remaining stock: {product.quantity}")

    def search_product(self, name):
        found = False
        for product in self.products.values():
            if name.lower() in product.name.lower():
                product.display_info()
                found = True
        if not found:
            print("Product not found.")

    def low_stock_alert(self, threshold=5):
        print(f"\nLOW STOCK ALERT (Threshold: {threshold})")
        for product in self.products.values():
            if product.quantity <= threshold:
                product.display_info()

    def display_all(self):
        if not self.products:
            print("Inventory is empty.")
            return
        print("\n--- INVENTORY LIST ---")
        for product in self.products.values():
            product.display_info()

    def total_inventory_value(self):
        total = sum(product.total_value() for product in self.products.values())
        print(f"\nTotal Inventory Value: ₹{total}")


def main():
    inventory = Inventory()

    while True:
        print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Restock Product")
        print("4. Sell Product")
        print("5. Search Product")
        print("6. Display All Products")
        print("7. Low Stock Alert")
        print("8. Total Inventory Value")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            pid = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            price = float(input("Enter Price: "))
            qty = int(input("Enter Quantity: "))
            inventory.add_product(pid, name, price, qty)

        elif choice == "2":
            pid = input("Enter Product ID to remove: ")
            inventory.remove_product(pid)

        elif choice == "3":
            pid = input("Enter Product ID to restock: ")
            amount = int(input("Enter quantity to add: "))
            inventory.restock_product(pid, amount)

        elif choice == "4":
            pid = input("Enter Product ID to sell: ")
            amount = int(input("Enter quantity to sell: "))
            inventory.sell_product(pid, amount)

        elif choice == "5":
            name = input("Enter product name to search: ")
            inventory.search_product(name)

        elif choice == "6":
            inventory.display_all()

        elif choice == "7":
            threshold = int(input("Enter low stock threshold (default 5): ") or 5)
            inventory.low_stock_alert(threshold)

        elif choice == "8":
            inventory.total_inventory_value()

        elif choice == "9":
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()