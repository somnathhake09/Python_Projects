class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks  # list of 3 marks
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