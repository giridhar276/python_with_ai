"""
Example 1: Generate Fernet Encryption Key

Install:
pip install cryptography

Important:
Keep this key safe.
If the key is lost, encrypted data cannot be decrypted.
If the key is stolen, encrypted data can be decrypted by attacker.
"""

from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("secret.key", "wb") as key_file:
    key_file.write(key)

print("Encryption key generated and saved to secret.key")
print("Do not commit this key to GitHub.")
