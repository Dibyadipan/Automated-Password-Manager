# Manages password encryption & storage

import json
import os
from utils.encryption import Encryption

class PasswordManager:
    def __init__(self, key, filename="passwords.json"):
        self.encryption = Encryption(key)
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return {}

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.data, file, indent=4)

    def add_password(self, site, username, password):
        encrypted_password = self.encryption.encrypt(password)
        self.data[site] = {"username": username, "password": encrypted_password}
        self.save_data()

    def retrieve_password(self, site):
        if site in self.data:
            encrypted_password = self.data[site]["password"]
            return self.encryption.decrypt(encrypted_password)
        return None

# # Example usage
# if __name__ == "__main__":
#     key = "supersecurekey123"
#     manager = PasswordManager(key)

#     # Adding password
#     manager.add_password("github.com", "myuser", "mypassword123")

#     # Retrieving password
#     print("Retrieved Password:", manager.retrieve_password("github.com"))
