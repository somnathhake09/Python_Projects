class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks  # list of 3 marks
    def calculate_percentage(self):
        total = sum(self.marks)
        percentage = total / len(self.marks)
        return percentage