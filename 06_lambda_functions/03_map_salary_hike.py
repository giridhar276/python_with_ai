# Topic: Lambda Functions
# Example: Salary hike using map

salaries = [50000, 65000, 80000]

# map() applies lambda logic to each salary.
updated_salaries = list(map(lambda salary: salary * 1.10, salaries))

print(updated_salaries)
