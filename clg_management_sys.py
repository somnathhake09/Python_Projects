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


# ===== HYBRID INHERITANCE =====
# Combination of Hierarchical (Person -> Student, Teacher)
# + Multiple (TeachingAssistant from Student & Teacher) = Hybrid structure
# (already built above — TeachingAssistant is the hybrid part)


def main():
    print("=== College Management Demo ===\n")

    s1 = Student("Somnath", 21, "S101")
    print("--- Student ---")
    s1.show_info()
    s1.study()

    t1 = Teacher("Mrs. Sharma", 40, "Python Programming")
    print("\n--- Teacher ---")
    t1.show_info()
    t1.teach()

    ta1 = TeachingAssistant("Rahul", 23, "S202", "Data Structures", 5000)
    print("\n--- Teaching Assistant (Multiple + Hybrid) ---")
    ta1.show_info()
    ta1.study()
    ta1.teach()
    ta1.assist()


if __name__ == "__main__":
    main()