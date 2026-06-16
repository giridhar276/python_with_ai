# Topic: Lambda Functions
# Example: Total sales using reduce

from functools import reduce

sales = [10000, 20000, 15000, 30000]

# reduce() combines all sales values into one total.
total_sales = reduce(lambda total, amount: total + amount, sales)

print(total_sales)
