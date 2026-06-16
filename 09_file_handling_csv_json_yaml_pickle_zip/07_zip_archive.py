# Topic: File Handling
# Example: Create and extract ZIP

import os
import zipfile

root = os.path.dirname(os.path.dirname(__file__))
data_file = os.path.join(root, "data", "employees.csv")
zip_file = os.path.join(root, "outputs", "training_archive.zip")
extract_folder = os.path.join(root, "outputs", "extracted_files")

os.makedirs(os.path.dirname(zip_file), exist_ok=True)

# ZipFile is used to create the ZIP archive.
with zipfile.ZipFile(zip_file, "w") as zip_obj:
    zip_obj.write(data_file, arcname="employees.csv")

# ZipFile is used to read and extract the ZIP archive.
with zipfile.ZipFile(zip_file, "r") as zip_obj:
    zip_obj.extractall(extract_folder)

print(zip_file)
print(extract_folder)
