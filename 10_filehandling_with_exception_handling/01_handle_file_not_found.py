# Topic: Exception Handling
# Example: Handle missing file

try:
    with open("missing_file.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found. Please check the path.")
