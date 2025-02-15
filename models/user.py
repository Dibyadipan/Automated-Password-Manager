# Handles user authentication

import hashlib
import json
import os

class UserManager:
    def __init__(self, filename="users.json"):
        self.filename = filename
        self.users = self.load_users()

    def load_users(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return {}

    def save_users(self):
        with open(self.filename, "w") as file:
            json.dump(self.users, file, indent=4)

    def register(self, username, password):
        if username in self.users:
            print("User already exists!")
            return False
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.users[username] = hashed_password
        self.save_users()
        print("User registered successfully!")
        return True

    def login(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if self.users.get(username) == hashed_password:
            print("Login successful!")
            return True
        print("Invalid credentials!")
        return False

# # Example usage
# if __name__ == "__main__":
#     user_manager = UserManager()

#     # Register a new user
#     user_manager.register("admin", "securepassword123")

#     # Attempt login
#     user_manager.login("admin", "securepassword123")
