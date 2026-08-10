# ===== Base Class =====
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


# ===== HIERARCHICAL INHERITANCE =====
# Two classes (Student, Teacher) inherit from SAME base class (Person)

class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def show_info(self):
        super().show_info()
        print(f"Roll No: {self.roll_no}")

    def study(self):
        print(f"{self.name} is studying.")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def show_info(self):
        super().show_info()
        print(f"Subject: {self.subject}")

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")


# ===== MULTIPLE INHERITANCE =====
# TeachingAssistant inherits from TWO classes: Student AND Teacher

class TeachingAssistant(Student, Teacher):
    def __init__(self, name, age, roll_no, subject, stipend):
        Student.__init__(self, name, age, roll_no)
        Teacher.__init__(self, name, age, subject)
        self.stipend = stipend

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        print(f"Roll No: {self.roll_no}, Subject: {self.subject}")
        print(f"Stipend: ₹{self.stipend}")

    def assist(self):
        print(f"{self.name} is assisting in {self.subject} class while also studying.")

