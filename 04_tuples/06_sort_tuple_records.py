# Topic: Tuples
# Example: Sort tuple records

products = [("Laptop", 30), ("Mouse", 120), ("Keyboard", 80)]

# sorted() returns a new list sorted by quantity.
sorted_products = sorted(products, key=lambda item: item[1], reverse=True)

print(sorted_products)
