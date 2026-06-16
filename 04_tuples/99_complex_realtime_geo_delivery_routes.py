# Topic: Complex Tuples
# Example: Delivery route scoring

from math import sqrt

warehouse = ("Warehouse", 12.9716, 77.5946)

delivery_points = [
    ("CustomerA", 12.9352, 77.6245),
    ("CustomerB", 13.0358, 77.5970),
    ("CustomerC", 12.9141, 77.6101),
]

warehouse_name, warehouse_lat, warehouse_lon = warehouse

for customer_name, customer_lat, customer_lon in delivery_points:
    # sqrt() calculates square root for distance score.
    distance_score = sqrt((warehouse_lat - customer_lat) ** 2 + (warehouse_lon - customer_lon) ** 2)

    # round() formats distance score.
    print(customer_name, round(distance_score, 4))
