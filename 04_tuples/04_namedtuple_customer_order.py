# Topic: Tuples
# Example: namedtuple order

from collections import namedtuple

# namedtuple() creates a tuple type with readable field names.
Order = namedtuple("Order", ["order_id", "customer", "amount"])

order = Order("O1001", "IBM", 120000)

print(order.order_id, order.customer, order.amount)
