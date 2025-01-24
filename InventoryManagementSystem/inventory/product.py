# product.py

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # Method to update the quantity of the product
    def update_quantity(self, new_quantity):
        if new_quantity >= 0:
            self.quantity = new_quantity
        else:
            print("Quantity cannot be negative.")

    # Method to update the price of the product
    def update_price(self, new_price):
        if new_price >= 0:
            self.price = new_price
        else:
            print("Price cannot be negative.")

    # Method to get a string representation of the product's information
    def get_product_info(self):
        return f"Product: {self.name}\nPrice: {self.price} USD\nQuantity: {self.quantity}"

# Example usage of the class:
if __name__ == "__main__":
    # Create a product
    product = Product("Laptop", 1000, 5)

    # Display product information
    print(product.get_product_info())

    # Update the product's quantity
    product.update_quantity(10)
    print("\nAfter updating the quantity:")
    print(product.get_product_info())

    # Update the product's price
    product.update_price(950)
    print("\nAfter updating the price:")
    print(product.get_product_info())

Items = [
    {
        "name": "Toshiba",
        "description": "Laptop with 16GB RAM",
        "sku": "SKU0001",
        "quantity": 400,
        "unitPrice": 100,
        "purchasePrice": 80,
        "profit_rate": 20,
        "currency": "EUR",
    },
    {
        "name": "applebook",
        "description": "Laptop with 8GB RAM",
        "sku": "SKU0002",
        "quantity": 7000,
        "unitPrice": 20,
        "purchasePrice": 15,
        "profit_rate": 25,
        "currency": "EUR",
    },
    {
        "name": "macbook pro 2020",
        "description": "Laptop with 16GB RAM",
        "sku": "SKU0003",
        "quantity": 700,
        "unitPrice": 2000,
        "purchasePrice": 1500,
        "profit_rate": 25,
        "currency": "EUR",
    },
]
