def calc_average(marks):
    """
    Calculate the average of a list of marks.

    Args:
        marks (list of int or float): List containing the marks.

    Returns:
        float: The average of the marks.
    """
    total = 0
    # Sum all marks
    for m in marks:
        total += m
    # Calculate average
    average = total / len(marks)
    return average  # Fixed typo

# List of marks
marks = [85, 90, 78, 92]

# Print the average score
print("Average Score is", calc_average(marks))