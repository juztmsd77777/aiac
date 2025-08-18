import json, os   # Import JSON for saving data, os for file checking

FILE = "users.json"   # File where usernames & passwords will be stored

def load_users():
    """Load users from file, return empty dict if file doesn't exist."""
    return json.load(open(FILE)) if os.path.exists(FILE) else {}

def save_users(users):
    """Save users to file in JSON format."""
    json.dump(users, open(FILE, "w"))

def register():
    """Register a new user by asking for username & password."""
    users = load_users()  # Load existing users
    u = input("New username: ")  # Ask for username
    if u in users:               # Prevent duplicate usernames
        return print("User already exists!")
    p = input("New password: ")  # Ask for password
    users[u] = p                 # Save new user
    save_users(users)            # Write back to file
    print("✅ Registered successfully!")

def login():
    """Login by checking username & password."""
    users = load_users()  # Load saved users
    u = input("Username: ")
    p = input("Password: ")
    if users.get(u) == p:   # Check credentials
        print(f"✅ Welcome, {u}!")
    else:
        print("❌ Invalid login")

# Main menu loop
while True:
    print("\n--- Menu ---")
    print("1. Register\n2. Login\n3. Exit")
    ch = input("Choose: ")
    if ch == "1": register()
    elif ch == "2": login()
    elif ch == "3": break
    else: print("Invalid choice")
