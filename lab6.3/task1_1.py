class Student:
    def __init__(self):
        self.name = ""
        self.roll_no = ""
        self.marks = 0

    def set_details(self, name, roll_no, marks):
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


# Example usage
s = Student()
s.set_details("John Doe", "12345", 85)
s.display_details()
print(f"Grade: {s.calculate_grade()}")
