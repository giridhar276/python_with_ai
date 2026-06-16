"""
Example 4: Wrong Key Decryption Failure

Concept:
Encrypted data can only be decrypted using the correct key.
"""

from cryptography.fernet import Fernet, InvalidToken

correct_key = Fernet.generate_key()
wrong_key = Fernet.generate_key()

correct_fernet = Fernet(correct_key)
wrong_fernet = Fernet(wrong_key)

message = "Highly confidential information"

encrypted_message = correct_fernet.encrypt(message.encode("utf-8"))

try:
    decrypted_message = wrong_fernet.decrypt(encrypted_message)
    print("Decrypted Message:", decrypted_message.decode("utf-8"))

except InvalidToken:
    print("Decryption failed because wrong key was used.")
