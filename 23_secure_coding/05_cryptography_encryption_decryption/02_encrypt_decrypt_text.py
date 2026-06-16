"""
Example 2: Encrypt and Decrypt Text Using Fernet

Run:
python 01_generate_fernet_key.py
python 02_encrypt_decrypt_text.py
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

plain_text = "Customer account number: 123456789"

encrypted_data = fernet.encrypt(plain_text.encode("utf-8"))
decrypted_data = fernet.decrypt(encrypted_data).decode("utf-8")

print("Plain Text:", plain_text)
print("Encrypted Data:", encrypted_data.decode("utf-8"))
print("Decrypted Data:", decrypted_data)
