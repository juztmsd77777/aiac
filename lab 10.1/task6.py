def grade(score):
    """
    Converts a numeric score to a letter grade.
    
    Args:
        score (int/float): The numeric score (0-100)
    
    Returns:
        str: Letter grade (A, B, C, D, or F)
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Example usage with readable output
test_scores = [95, 82, 67, 45, 73]

print("Grade Report:")
print("-" * 20)
for score in test_scores:
    letter_grade = grade(score)
    print(f"Score: {score:3d} → Grade: {letter_grade}")