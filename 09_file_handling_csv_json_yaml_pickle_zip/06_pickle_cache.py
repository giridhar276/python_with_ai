# Topic: File Handling
# Example: Pickle cache

import os
import pickle

cache_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs", "cache.pkl")
os.makedirs(os.path.dirname(cache_file), exist_ok=True)

cache_data = {"processed_files": 10, "status": "success"}

with open(cache_file, "wb") as file:
    # pickle.dump() saves Python object in binary format.
    pickle.dump(cache_data, file)

with open(cache_file, "rb") as file:
    # pickle.load() reads Python object from binary format.
    loaded_cache = pickle.load(file)

print(loaded_cache)
