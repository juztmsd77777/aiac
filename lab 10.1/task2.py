def area_of_rectangle(length, breadth):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle. Must be positive.
        breadth (float): The breadth of the rectangle. Must be positive.

    Returns:
        float: The area of the rectangle.

    Raises:
        TypeError: If length or breadth is not a number.
        ValueError: If length or breadth is not positive.
    """
    if not isinstance(length, (int, float)):
        raise TypeError("Length must be a number (int or float).")
    if not isinstance(breadth, (int, float)):
        raise TypeError("Breadth must be a number (int or float).")
    if length <= 0:
        raise ValueError("Length must be positive.")
    if breadth <= 0:
        raise ValueError("Breadth must be positive.")

    return length * breadth


if __name__ == "__main__":
    # Example usage of area_of_rectangle function
    length = 10
    breadth = 20
    area = area_of_rectangle(length, breadth)
    print(f"Area of rectangle whose length is {length} and breadth is {breadth}: {area}")
   
    # Additional example use cases
    examples = [
        (5, 8),
        (12.5, 4),
        (7, 7),
        (3.2, 6.1),
    ]
    for l, b in examples:
        try:
            area = area_of_rectangle(l, b)
            print(f"Area of rectangle whose length is {l} and breadth is {b}: {area}")
        except (TypeError, ValueError) as e:
            print(f"Error with length={l}, breadth={b}: {e}")