"""
Mini Projects: Student Report Card Generator 
Concept Coverd:VARIABLES in Python

This Project Shows how variables are used to :
1. Store different data types(string, int, float, boolean)
2. Take user input and store it in variables
3. Perform calculations using variables
4. Update / reassign variable values
5. Use variables in inside formatted strings (f-strings)
"""

# Declaring variables(string, int type)
student_name= "somnath hake"
roll_number= 9
student_class= "10th"

# Taking user input and storing it in variables

student_name= input("Enter Student Name: ")
roll_number= int(input("Enter Roll Number: "))
student_class= input("Enter Student Class: ")

#storing marks in variables
marks_maths= int(input("Enter marks in Maths: "))
marks_Marathi= int(input("Enter marks in Marathi: "))
marks_english= int(input("Enter marks in English: "))

#using variables to perform calculations
total_subjects= 3
total_marks= marks_maths + marks_Marathi + marks_english
percentage= total_marks / total_subjects

# boolean variable (true/false) based on condition
is_pass= percentage >= 35

# Reassigning variable values
grade = "F"

if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 35:
    grade = "C"

# Displaying the report card using variables inside formatted strings (f-strings)

print("\n\n********** Student Report Card **********")
print(f"Student Name: {student_name}")
print(f"Roll Number: {roll_number}")
print(f"Student Class: {student_class}")
print("-----------------------------------------")

print(f"Maths  : {marks_maths}")
print(f"Marathi: {marks_Marathi}")
print(f"English: {marks_english}")
print("-----------------------------------------")

print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"Result: {'Pass' if is_pass else 'Fail'}")
print("*****************************************")
