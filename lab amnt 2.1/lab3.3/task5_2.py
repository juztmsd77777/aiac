def convert_temp(value, from_unit, to_unit):
    from_unit, to_unit = from_unit.lower(), to_unit.lower()

    if from_unit == "c":
        c = value
    elif from_unit == "f":
        c = (value - 32) * 5/9
    elif from_unit == "k":
        c = value - 273.15
    else:
        return "Invalid from_unit"

    if to_unit == "c":
        return c
    elif to_unit == "f":
        return (c * 9/5) + 32
    elif to_unit == "k":
        return c + 273.15
    else:
        return "Invalid to_unit"

# Example calls
print(convert_temp(0, "c", "f"))   # Output: 32.0
print(convert_temp(32, "f", "c"))  # Output: 0.0
print(convert_temp(0, "c", "k"))   # Output: 273.15
