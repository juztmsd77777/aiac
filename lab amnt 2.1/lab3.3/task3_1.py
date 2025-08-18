def calculate_power_bill():
    try:
        units = float(input("Enter the number of units consumed: "))
        if units < 0:
            print("Units consumed cannot be negative.")
            return

        if units <= 100:
            bill = units * 5
        elif units <= 200:
            bill = 100 * 5 + (units - 100) * 7
        else:
            bill = 100 * 5 + 100 * 7 + (units - 200) * 10

        service_charge = 50
        total_bill = bill + service_charge

        print(f"Total power bill (including Rs.50 service charge): Rs. {total_bill:.2f}")
    except ValueError:
        print("Invalid input: Please enter a valid number for units consumed.")


calculate_power_bill()
