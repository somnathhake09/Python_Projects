"""
Smart Home Automation System
A daily-life mini project demonstrating OOP concepts:
- Encapsulation
- Inheritance
- Polymorphism
- Composition
- Abstraction (via simple menu interface)
"""


# ---------------- Base Class ----------------
class Device:
    """Base class for all smart devices."""

    def __init__(self, name):
        self.name = name          # public attribute
        self.__is_on = False      # encapsulated (private) attribute

    def turn_on(self):
        self.__is_on = True
        print(f"{self.name} turned ON.")

    def turn_off(self):
        self.__is_on = False
        print(f"{self.name} turned OFF.")

    def is_on(self):
        return self.__is_on

    def status(self):
        state = "ON" if self.__is_on else "OFF"
        return f"{self.name} is currently {state}."


# ---------------- Derived Classes (Inheritance) ----------------
class Light(Device):
    def __init__(self, name):
        super().__init__(name)
        self.__brightness = 0   # 0 to 100

    def set_brightness(self, level):
        if not self.is_on():
            print(f"{self.name} is OFF. Turn it on first.")
            return
        if 0 <= level <= 100:
            self.__brightness = level
            print(f"{self.name} brightness set to {level}%.")
        else:
            print("Brightness must be between 0 and 100.")

    def status(self):  # Polymorphism: overriding base method
        base_status = super().status()
        return f"{base_status} Brightness: {self.__brightness}%."


class Fan(Device):
    def __init__(self, name):
        super().__init__(name)
        self.__speed = 0   # 0 to 5

    def set_speed(self, speed):
        if not self.is_on():
            print(f"{self.name} is OFF. Turn it on first.")
            return
        if 0 <= speed <= 5:
            self.__speed = speed
            print(f"{self.name} speed set to {speed}.")
        else:
            print("Speed must be between 0 and 5.")

    def status(self):  # Polymorphism: overriding base method
        base_status = super().status()
        return f"{base_status} Speed: {self.__speed}."


class AC(Device):
    def __init__(self, name):
        super().__init__(name)
        self.__temperature = 24   # default temperature

    def set_temperature(self, temp):
        if not self.is_on():
            print(f"{self.name} is OFF. Turn it on first.")
            return
        if 16 <= temp <= 30:
            self.__temperature = temp
            print(f"{self.name} temperature set to {temp}°C.")
        else:
            print("Temperature must be between 16 and 30°C.")

    def status(self):  # Polymorphism: overriding base method
        base_status = super().status()
        return f"{base_status} Temperature: {self.__temperature}°C."


class TV(Device):
    def __init__(self, name):
        super().__init__(name)
        self.__volume = 10   # 0 to 100
        self.__channel = 1

    def set_volume(self, volume):
        if not self.is_on():
            print(f"{self.name} is OFF. Turn it on first.")
            return
        if 0 <= volume <= 100:
            self.__volume = volume
            print(f"{self.name} volume set to {volume}.")
        else:
            print("Volume must be between 0 and 100.")

    def set_channel(self, channel):
        if not self.is_on():
            print(f"{self.name} is OFF. Turn it on first.")
            return
        self.__channel = channel
        print(f"{self.name} channel changed to {channel}.")

    def status(self):  # Polymorphism: overriding base method
        base_status = super().status()
        return f"{base_status} Volume: {self.__volume}, Channel: {self.__channel}."


# ---------------- Composition ----------------
class SmartHome:
    """SmartHome HAS-A collection of devices (Composition)."""

    def __init__(self, home_name):
        self.home_name = home_name
        self.devices = {}   # name -> Device object

    def add_device(self, device):
        self.devices[device.name] = device
        print(f"{device.name} added to {self.home_name}.")

    def remove_device(self, name):
        if name in self.devices:
            del self.devices[name]
            print(f"{name} removed from {self.home_name}.")
        else:
            print("Device not found.")

    def get_device(self, name):
        return self.devices.get(name)

    def turn_on_all(self):
        for device in self.devices.values():
            device.turn_on()

    def turn_off_all(self):
        for device in self.devices.values():
            device.turn_off()

    def show_all_status(self):
        if not self.devices:
            print("No devices added yet.")
            return
        print(f"\n--- {self.home_name}: Device Status ---")
        for device in self.devices.values():
            print(device.status())   # Polymorphism in action


# ---------------- Menu-driven Program ----------------
def main():
    home = SmartHome("My Home")

    while True:
        print("\n===== SMART HOME AUTOMATION MENU =====")
        print("1. Add Device")
        print("2. Remove Device")
        print("3. Turn ON a Device")
        print("4. Turn OFF a Device")
        print("5. Set Device Property (brightness/speed/temperature/volume)")
        print("6. Turn ON All Devices")
        print("7. Turn OFF All Devices")
        print("8. Show All Device Status")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            print("Device types: 1-Light  2-Fan  3-AC  4-TV")
            dtype = input("Select device type (1-4): ")
            name = input("Enter device name (e.g., Living Room Light): ")

            if dtype == '1':
                home.add_device(Light(name))
            elif dtype == '2':
                home.add_device(Fan(name))
            elif dtype == '3':
                home.add_device(AC(name))
            elif dtype == '4':
                home.add_device(TV(name))
            else:
                print("Invalid device type.")

        elif choice == '2':
            name = input("Enter device name to remove: ")
            home.remove_device(name)

        elif choice == '3':
            name = input("Enter device name to turn ON: ")
            device = home.get_device(name)
            if device:
                device.turn_on()
            else:
                print("Device not found.")

        elif choice == '4':
            name = input("Enter device name to turn OFF: ")
            device = home.get_device(name)
            if device:
                device.turn_off()
            else:
                print("Device not found.")

        elif choice == '5':
            name = input("Enter device name: ")
            device = home.get_device(name)
            if not device:
                print("Device not found.")
                continue

            if isinstance(device, Light):
                level = int(input("Enter brightness (0-100): "))
                device.set_brightness(level)
            elif isinstance(device, Fan):
                speed = int(input("Enter speed (0-5): "))
                device.set_speed(speed)
            elif isinstance(device, AC):
                temp = int(input("Enter temperature (16-30): "))
                device.set_temperature(temp)
            elif isinstance(device, TV):
                sub_choice = input("Set (1) Volume or (2) Channel? ")
                if sub_choice == '1':
                    vol = int(input("Enter volume (0-100): "))
                    device.set_volume(vol)
                elif sub_choice == '2':
                    ch = int(input("Enter channel number: "))
                    device.set_channel(ch)

        elif choice == '6':
            home.turn_on_all()

        elif choice == '7':
            home.turn_off_all()

        elif choice == '8':
            home.show_all_status()

        elif choice == '9':
            print("Exiting Smart Home Automation System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()