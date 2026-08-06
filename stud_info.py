class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def calculate_percentage(self):
        total = sum(self.marks)
        percentage = total / len(self.marks)
        return percentage

    def calculate_grade(self):
        percentage = self.calculate_percentage()
        
        if percentage >= 90:
            return "A+"
        elif percentage >= 75:
            return "A"
        elif percentage >= 60:
            return "B"
        elif percentage >= 40:
            return "C"
        else:
            return "Fail"

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")
        print(f"Percentage: {self.calculate_percentage():.2f}%")
        print(f"Grade: {self.calculate_grade()}")
        print("-" * 30)


s1 = Student("Somnath", 1, [90, 85, 95])
s2 = Student("Dikshu", 2, [60, 55, 70])

s1.display_info()
s2.display_info()