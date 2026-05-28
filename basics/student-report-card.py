# Student Report Card — OOP Practice
# Demonstrates Classes, Objects, Methods and Constructors in Python
# Creates a Student object and displays their report with grade

class Student:
    
    # Constructor — runs automatically when object is created
    def __init__(self, name, roll, marks):
        self.name = name      # Student's name
        self.roll = roll      # Roll number
        self.marks = marks    # Marks out of 100
    
    # Method to calculate grade based on marks
    def calculate_grade(self):
        if self.marks >= 75:
            return "Grade A — Excellent"
        elif self.marks >= 50:
            return "Grade B — Good"
        else:
            return "Grade C — Needs Improvement"
    
    # Method to display full student report
    def display(self):
        print("---- Student Report ----")
        print("Name       :", self.name)
        print("Roll Number:", self.roll)
        print("Marks      :", self.marks)
        print("Grade      :", self.calculate_grade())
        print("------------------------")


# Creating Student objects
student1 = Student("Ishika", 101, 88)
student1.display()

student2 = Student("Rahul", 102, 55)
student2.display()

student3 = Student("Priya", 103, 40)
student3.display()
