"""
Example 3: Encrypt and Decrypt File

Use Case:
Protect local sensitive files.

Run:
python 01_generate_fernet_key.py
python 03_encrypt_decrypt_file.py
"""

from cryptography.fernet import Fernet
from pathlib import Path

key_path = Path("secret.key")

if not key_path.exists():
    print("secret.key not found.")
    print("Please run 01_generate_fernet_key.py first.")
    raise SystemExit

key = key_path.read_bytes()
fernet = Fernet(key)

plain_file = Path("customer_data.txt")
encrypted_file = Path("customer_data.encrypted")
decrypted_file = Path("customer_data_decrypted.txt")

plain_file.write_text("Name: Ravi\nAccount: 987654321\nBalance: 50000", encoding="utf-8")

plain_data = plain_file.read_bytes()
encrypted_data = fernet.encrypt(plain_data)

encrypted_file.write_bytes(encrypted_data)

decrypted_data = fernet.decrypt(encrypted_file.read_bytes())
decrypted_file.write_bytes(decrypted_data)

print("Original file created:", plain_file)
print("Encrypted file created:", encrypted_file)
print("Decrypted file created:", decrypted_file)
