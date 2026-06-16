# Topic: Tuples
# Example: Return multiple values

def calculate_invoice(amount, tax_percent):
    tax = amount * tax_percent / 100
    total = amount + tax
    return tax, total

tax_amount, final_amount = calculate_invoice(10000, 18)

print(tax_amount, final_amount)
