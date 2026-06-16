"""
Example 1: Hash Text Using SHA256

Use Case:
- Create fingerprint of data
- Verify if text changed
- Store non-reversible representation

Important:
Hashing is not encryption.
A hash cannot be decrypted.
"""

import hashlib

message = "Hello Secure Python"

hash_object = hashlib.sha256(message.encode("utf-8"))
hash_value = hash_object.hexdigest()

print("Original Message:", message)
print("SHA256 Hash:", hash_value)
