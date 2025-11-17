def welcome_students(students):
    """
    Prints a welcome message for each student in the provided list.
    
    Args:
        students (list): A list of student names (strings)
    
    Returns:
        None: This function prints output but doesn't return a value
    """
    # Iterate through each student in the list
    for student in students:
        # Print welcome message for current student
        print("Welcome", student)


# Create list of student names
students = ["Alice", "Bob", "Charlie"]

# Call function to welcome all students
welcome_students(students)