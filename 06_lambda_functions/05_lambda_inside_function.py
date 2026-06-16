# Topic: Lambda Functions
# Example: Dynamic tax calculator

def tax_calculator(tax_percent):
    return lambda amount: amount + (amount * tax_percent / 100)

gst_18 = tax_calculator(18)

print(gst_18(10000))
