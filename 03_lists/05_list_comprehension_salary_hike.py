# Topic: Lists
# Example: Salary hike using list comprehension

salaries = [50000, 65000, 80000, 95000]

updated_salaries = [salary + salary * 0.10 for salary in salaries]

print(updated_salaries)
