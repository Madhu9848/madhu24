# login.py

def login(username, password):
    """
    Simple login function that validates username and password.
    """
    valid_user = "admin"
    valid_password = "password123"

    if username == valid_user and password == valid_password:
        return "Login successful"
    else:
        return "Invalid credentials"

# Example usage:
if __name__ == "__main__":
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    print(login(user, pwd))
