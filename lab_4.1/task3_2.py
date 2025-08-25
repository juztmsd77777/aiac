def extract_student_info(data):
    """
    Navigates a nested dictionary of the form:
    {
        "student": {
            "personal": {
                "first_name": ...,
                "last_name": ...
            },
            "academic": {
                "branch": ...,
                "sgpa": ...
            }
        }
    }
    and returns (Full Name, Branch, SGPA)
    """
    try:
        personal = data["student"]["personal"]
        academic = data["student"]["academic"]
        first_name = personal.get("first_name", "")
        last_name = personal.get("last_name", "")
        branch = academic.get("branch", "")
        sgpa = academic.get("sgpa", None)
        full_name = f"{first_name} {last_name}".strip()
        return (full_name, branch, sgpa)
    except (KeyError, TypeError):
        return ("", "", None)

if __name__ == "__main__":
    # Get user input for student details
    while True:
        first_name = input("First name: ").strip()
        if not first_name:
            print("First name cannot be empty. Please enter a valid first name.")
        else:
            break
    while True:
        last_name = input("Last name: ").strip()
        if not last_name:
            print("Last name cannot be empty. Please enter a valid last name.")
        else:
            break
    branch = input("Branch: ").strip()
    while True:
        sgpa_input = input("SGPA: ").strip()
        try:
            sgpa = float(sgpa_input)
            break
        except ValueError:
            print("Please enter a valid SGPA (number).")

    # Build the nested dictionary as specified
    student_data = {
        "student": {
            "personal": {
                "first_name": first_name,
                "last_name": last_name
            },
            "academic": {
                "branch": branch,
                "sgpa": sgpa
            }
        }
    }

    result = extract_student_info(student_data)
    print(result)
    print(f"Full Name: {result[0]}")
    print(f"Branch: {result[1]}")
    print(f"SGPA: {result[2]}")
