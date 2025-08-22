class SRU_Student:
    def __init__(self, name, roll_no, department):
        self.name = name
        self.roll_no = roll_no
        self.department = department

    def Student_Data(self, filename="student_data.txt"):
        data = (
            f"Name: {self.name}\n"
            f"Roll No: {self.roll_no}\n"
            f"Department: {self.department}\n"
        )
        with open(filename, "w") as file:
            file.write(data)
        print("Student Data:")
        print(data)
        print(f"Student data saved to {filename}")
# Example usage:
student = SRU_Student("VVR", "259", "Computer Science")
student.Student_Data()

