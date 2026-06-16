# Topic: Conditions
# Example: Employee bonus eligibility

salary = 85000
rating = 4.6

if rating >= 4.5:
    bonus_percentage = 20
elif rating >= 4.0:
    bonus_percentage = 12
elif rating >= 3.5:
    bonus_percentage = 8
else:
    bonus_percentage = 0

bonus_amount = salary * bonus_percentage / 100

print("Salary:", salary)
print("Rating:", rating)
print("Bonus Percentage:", bonus_percentage)
print("Bonus Amount:", bonus_amount)
