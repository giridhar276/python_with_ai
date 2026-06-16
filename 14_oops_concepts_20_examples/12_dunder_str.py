# Topic: OOP Concepts
# Example: 12 dunder str

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} costs {self.price}'

print(Product('Laptop', 65000))
