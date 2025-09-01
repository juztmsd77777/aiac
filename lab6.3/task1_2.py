class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "Fail"


# Managing multiple students
students = []

# Adding students
students.append(Student("John Doe", "12345", 85))
students.append(Student("Alice", "12346", 92))
students.append(Student("Bob", "12347", 58))

# Display all students
for s in students:
    s.display_details()
    print(f"Grade: {s.calculate_grade()}")
    print("-" * 30)
