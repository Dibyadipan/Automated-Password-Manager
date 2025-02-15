# AES encryption for encrypting passwords before storing
# We'll use AES encryption (PyCryptodome library)

from Crypto.Cipher import AES
import base64

class Encryption:
    def __init__(self, key):
        self.key = key.ljust(32)[:32].encode()  # Ensure key is 32 bytes

    def encrypt(self, plain_text):
        cipher = AES.new(self.key, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(plain_text.encode())
        return base64.b64encode(nonce + ciphertext).decode()

    def decrypt(self, encrypted_text):
        encrypted_data = base64.b64decode(encrypted_text)
        nonce = encrypted_data[:16]
        ciphertext = encrypted_data[16:]
        cipher = AES.new(self.key, AES.MODE_EAX, nonce=nonce)
        return cipher.decrypt(ciphertext).decode()

# # Example usage
# if __name__ == "__main__":
#     key = "supersecurekey123"  # Store securely in real use cases
#     encryption = Encryption(key)

#     encrypted = encryption.encrypt("mypassword123")
#     print("Encrypted:", encrypted)

#     decrypted = encryption.decrypt(encrypted)
#     print("Decrypted:", decrypted)

