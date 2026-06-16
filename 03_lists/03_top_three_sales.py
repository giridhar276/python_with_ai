# Topic: Lists
# Example: Top three sales

sales = [90000, 120000, 45000, 150000, 70000]

# sorted() returns a new sorted list.
top_three = sorted(sales, reverse=True)[:3]

print(top_three)
