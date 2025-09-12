#this is class for sru student and it takes name,roll_no, hostel_status as input and it has a method to update the fee status and displaydetails
class sru_student:
    # Constructor method to initialize student object with basic details
    def __init__(self, name, roll_no, hostel_status):
        # Store student's name
        self.name = name
        # Store student's roll number
        self.roll_no = roll_no
        # Store whether student lives in hostel or not
        self.hostel_status = hostel_status
        # Initialize fee payment status as False (not paid)
        self.fee_paid = False
    
    # Method to update the fee payment status of the student
    def fee_update(self, fee_status):
        # Update the fee payment status
        self.fee_paid = fee_status
        # Display appropriate message based on fee status
        if fee_status:
            print(f"Fee payment updated: {self.name} has paid the fees")
        else:
            print(f"Fee payment updated: {self.name} has not paid the fees")
    
    # Method to display all student details in a formatted way
    def display_details(self):
        # Print header separator
        print("=" * 40)
        print("SRU Student Details")
        print("=" * 40)
        # Display student name
        print(f"Name: {self.name}")
        # Display student roll number
        print(f"Roll Number: {self.roll_no}")
        # Display hostel status (Yes/No based on boolean value)
        print(f"Hostel Status: {'Yes' if self.hostel_status else 'No'}")
        # Display fee payment status (Paid/Not Paid based on boolean value)
        print(f"Fee Status: {'Paid' if self.fee_paid else 'Not Paid'}")
        # Print footer separator
        print("=" * 40)
if __name__ == "__main__":
    # Create a student object
    student1 = sru_student("John Doe", "SRU2024001", True)
    
    # Display initial details
    student1.display_details()
    
    # Update fee status
    student1.fee_update(True)
    
    # Display updated details
    student1.display_details()
    
    # Create another student
    student2 = sru_student("Jane Smith", "SRU2024002", False)
    student2.fee_update(False)
    student2.display_details()
