class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price *self.quantity

    def update_stock(self,amount):
        self.quantity +=amount

    def display_info(self):
        print(f"ID: {self.product_id} | Name: {self.name} | Price: ₹{self.price} | Qty: {self.quantity} | Total Value: ₹{self.total_value()}")