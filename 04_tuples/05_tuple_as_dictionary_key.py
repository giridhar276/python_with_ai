# Topic: Tuples
# Example: Tuple as dictionary key

sales_summary = {
    ("Bangalore", "Laptop"): 20,
    ("Bangalore", "Mouse"): 100,
    ("Hyderabad", "Laptop"): 12
}

key = ("Bangalore", "Laptop")

print(sales_summary[key])
