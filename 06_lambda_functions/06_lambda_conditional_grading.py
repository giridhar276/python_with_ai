# Topic: Lambda Functions
# Example: Conditional grading

grade_employee = lambda rating: "Excellent" if rating >= 4.5 else "Good" if rating >= 4.0 else "Average"

ratings = [4.8, 4.2, 3.6]

for rating in ratings:
    print(rating, grade_employee(rating))
