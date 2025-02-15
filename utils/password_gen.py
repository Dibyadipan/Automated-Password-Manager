# Secure password generator
# Generates strong random passwords 

import random
import string

class PasswordGenerator:
    def __init__(self, length=16):
        self.length = length

    def generate(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(self.length))
        return password

# # Example usage
# if __name__ == "__main__":
#     generator = PasswordGenerator(12)
#     print("Generated Password:", generator.generate())

