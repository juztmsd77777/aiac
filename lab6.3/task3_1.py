def age(n):
    if n <= 0 or n > 120:
        print("Invalid age")
    elif n <= 13:
        print("Child")
    elif n <= 19:
        print("Teenager")
    elif n <= 59:
        print("Adult")
    else:
        print("Senior")

age_input = int(input("Enter your age: "))
age(age_input)
