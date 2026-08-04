# 4. Student Grade Management
# Suggested Classes: Student, Subject, ReportCard, GradeCalculator
# Features: Marks, average, grades, report card
# OOP Concepts: Classes, Encapsulation, Abstraction

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

        # Encapsulation
        self.__subjects = []

    def add_subject(self, subject):
        self.__subjects.append(subject)

    def get_subjects(self):
        return self.__subjects


class Subject:
    def __init__(self, name, marks):
        self.name = name

        # Encapsulation
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Marks must be between 0 and 100.")


class GradeCalculator:

    # Abstraction
    def calculate_average(self, subjects):
        if not subjects:
            return 0

        total = 0

        for subject in subjects:
            total += subject.get_marks()

        return total / len(subjects)

    def calculate_grade(self, average):
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"


class ReportCard:
    def __init__(self, student):
        self.student = student
        self.calculator = GradeCalculator()

    def generate_report(self):
        subjects = self.student.get_subjects()

        average = self.calculator.calculate_average(subjects)
        grade = self.calculator.calculate_grade(average)

        print("\n========== REPORT CARD ==========")
        print("Name    :", self.student.name)
        print("Roll No :", self.student.roll_no)

        print("\nSubjects:")

        for subject in subjects:
            print(
                subject.name,
                "-",
                subject.get_marks()
            )

        print("\nAverage :", round(average, 2))
        print("Grade   :", grade)
        print("=================================")


# -------------------------
# Example Usage
# -------------------------

student = Student("Iqra", 101)

maths = Subject("Mathematics", 100)
python = Subject("Python", 98)
dbms = Subject("DBMS", 99)
dsa = Subject("DSA", 99)

student.add_subject(maths)
student.add_subject(python)
student.add_subject(dbms)
student.add_subject(dsa)

report = ReportCard(student)

report.generate_report()