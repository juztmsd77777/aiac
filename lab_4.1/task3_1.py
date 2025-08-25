def extract_student_info(data):
    """
    Extracts and returns a student's full name, branch, and SGPA from a nested dictionary.
    Returns a tuple: (Full Name, Branch, SGPA)
    """
    def find_keys(d):
        # Recursively search for required keys in nested dictionaries
        result = {'first_name': None, 'last_name': None, 'branch': None, 'sgpa': None}
        if isinstance(d, dict):
            for k, v in d.items():
                if k in result and result[k] is None:
                    result[k] = v
                elif isinstance(v, dict):
                    sub_result = find_keys(v)
                    for key in result:
                        if result[key] is None and sub_result[key] is not None:
                            result[key] = sub_result[key]
        return result

    info = find_keys(data)
    full_name = f"{info['first_name']} {info['last_name']}"
    return (full_name, info['branch'], info['sgpa'])

# Take user input
def get_student_input():
    print("Enter student information:")
    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()
    branch = input("Branch: ").strip()
    while True:
        try:
            sgpa = float(input("SGPA: ").strip())
            break
        except ValueError:
            print("Please enter a valid SGPA (number).")
    # For demonstration, wrap in a nested dictionary
    data = {
        "student": {
            "first_name": first_name,
            "last_name": last_name,
            "branch": branch,
            "sgpa": sgpa
        }
    }
    return data

if __name__ == "__main__":
    student_data = get_student_input()
    result = extract_student_info(student_data)
    print("Extracted Student Info:")
    print(f"Full Name: {result[0]}")
    print(f"Branch: {result[1]}")
    print(f"SGPA: {result[2]}")







