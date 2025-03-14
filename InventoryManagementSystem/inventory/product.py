class Product:
    def __init__(self, name, description, sku, quantity, unit_price, purchase_price, profit_rate, currency):
        self.name = name
        self.description = description
        self.sku = sku
        self.quantity = quantity
        self.unit_price = unit_price
        self.purchase_price = purchase_price
        self.profit_rate = profit_rate
        self.currency = currency

    def update_quantity(self, new_quantity):
        """Update the product quantity ensuring it is not negative."""
        if new_quantity >= 0:
            self.quantity = new_quantity
            return True
        else:
            print("Quantity cannot be negative.")
            return False

    def update_price(self, new_price):
        """Update the price of the product ensuring it is not negative."""
        if new_price >= 0:
            self.unit_price = new_price
            return True
        else:
            print("Price cannot be negative.")
            return False

    def calculate_profit(self):
        """Calculate profit for this product"""
        return (self.unit_price - self.purchase_price) * self.quantity

    def get_product_info(self):
        """Returns product details as a formatted string."""
        return (f"Name: {self.name}\n"
                f"Description: {self.description}\n"
                f"SKU: {self.sku}\n"
                f"Quantity: {self.quantity}\n"
                f"Unit Price: {self.unit_price} {self.currency}\n"
                f"Purchase Price: {self.purchase_price} {self.currency}\n"
                f"Profit Rate: {self.profit_rate}")