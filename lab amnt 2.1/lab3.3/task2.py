def sort_numbers():
    try:
        user_input = input("Enter numbers separated by spaces to sort: ")
        numbers = list(map(float, user_input.strip().split()))
        sorted_numbers = sorted(numbers)
        print("Sorted numbers:", ' '.join(str(int(num)) for num in sorted_numbers))
    except ValueError:
        print("Invalid input: Please enter only numbers separated by spaces.")
if __name__ == "__main__":
    sort_numbers()
