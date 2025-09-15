from typing import List

def average(numbers: List[float]) -> float:
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (List[float]): List of numeric values.

    Returns:
        float: The average of the numbers.

    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("The list is empty. Cannot compute average.")

    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    data = [80, 90, 100]
    print(f"Input: {data} → Average of this list: {average(data)}")

