# Topic: User Defined Functions
# Example: EMI calculation

def calculate_emi(principal, annual_rate, months):
    monthly_rate = annual_rate / 12 / 100
    emi = principal * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)

    # round() formats EMI to two decimal places.
    return round(emi, 2)

print(calculate_emi(500000, 9.5, 60))
