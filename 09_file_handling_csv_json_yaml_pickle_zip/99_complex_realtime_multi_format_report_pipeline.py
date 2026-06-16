# Topic: Complex File Handling
# Example: Multi-format report pipeline

import os
import csv
import json
import pickle
import zipfile

root = os.path.dirname(os.path.dirname(__file__))
output_folder = os.path.join(root, "outputs", "multi_format_report")

os.makedirs(output_folder, exist_ok=True)

summary = [
    {"department": "IT", "employees": 3},
    {"department": "HR", "employees": 1}
]

csv_file = os.path.join(output_folder, "summary.csv")

with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["department", "employees"])
    writer.writeheader()
    writer.writerows(summary)

json_file = os.path.join(output_folder, "summary.json")

with open(json_file, "w", encoding="utf-8") as file:
    json.dump(summary, file, indent=4)

pickle_file = os.path.join(output_folder, "summary.pkl")

with open(pickle_file, "wb") as file:
    pickle.dump(summary, file)

zip_file = os.path.join(root, "outputs", "multi_format_report.zip")

with zipfile.ZipFile(zip_file, "w") as archive:
    for file_name in os.listdir(output_folder):
        full_path = os.path.join(output_folder, file_name)
        archive.write(full_path, arcname=file_name)

print(zip_file)
