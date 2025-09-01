def age(n):
    if n <= 0 or n > 120:
        return "Invalid age"
    elif n <= 13:
        return "Child"
    elif n <= 19:
        return "Teenager"
    elif n <= 59:
        return "Adult"
    else:
        return "Senior"

# User input
age_input = int(input("Enter your age: "))
category = age(age_input)
print(f"Age: {age_input} → Category: {category}")
