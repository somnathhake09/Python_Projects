# Parent Class
class Vehicle:
    def __init__(self, brand, price_per_day):
        self.brand = brand
        self.price_per_day = price_per_day

    def display_info(self):
        print(f"Vehicle: {self.brand} | Rate: ${self.price_per_day}/day")


# Child Class 1 (Inherits from Vehicle)
class Car(Vehicle):
    def __init__(self, brand, price_per_day, seats):
        super().__init__(brand, price_per_day)  # Pass base info to parent
        self.seats = seats

    def display_info(self):
        print(f"Car: {self.brand} ({self.seats} seats) | Rate: ${self.price_per_day}/day")


# Child Class 2 (Inherits from Vehicle)
class Bike(Vehicle):
    def __init__(self, brand, price_per_day, helmet_included):
        super().__init__(brand, price_per_day)
        self.helmet_included = helmet_included

    def display_info(self):
        helmet_status = "Yes" if self.helmet_included else "No"
        print(f"Bike: {self.brand} (Helmet: {helmet_status}) | Rate: ${self.price_per_day}/day")


# --- Main Program ---
def calculate_total_rent(vehicle, days):
    total = vehicle.price_per_day * days
    print(f"Renting {vehicle.brand} for {days} days total: ${total}")


# Create objects
my_car = Car("Toyota", price_per_day=1000, seats=5)
my_bike = Bike("Yamaha", price_per_day=500, helmet_included=True)

# Use inherited and customized methods
print("--- AVAILABLE VEHICLES ---")
my_car.display_info()
my_bike.display_info()

print("\n--- RENTAL CALCULATIONS ---")
calculate_total_rent(my_car, days=3)
calculate_total_rent(my_bike, days=5)
