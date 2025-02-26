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

    # Method to update the quantity of the product
    def update_quantity(self, new_quantity):
        if new_quantity >= 0:
            self.quantity = new_quantity
        else:
            print("Quantity cannot be negative.")

    # Method to update the price of the product
    def update_price(self, new_price):
        if new_price >= 0:
            self.unit_price = new_price
        else:
            print("Price cannot be negative.")

    # Method to calculate profit
    def calculate_profit(self):
        return (self.unit_price - self.purchase_price) * self.quantity

    # Method to get a string representation of the product's information
    def get_product_info(self):
        return f"Name: {self.name}, SKU: {self.sku}, Preis: {self.unit_price} {self.currency}, Lagerbestand: {self.quantity}"
    
def get_total_inventory_value(self):
    """Berechnen Sie den Gesamtbestandswert, indem Sie die Werte aller Produkte addieren."""
    if not self.inventory:
        print("Das Inventar ist leer!")
        return 0  # Gibt 0 zurück, wenn das Inventar leer ist

    total_value = sum(product.unit_price * product.quantity for product in self.inventory.values())
    
    print(f"Gesamtwert des Inventars: {total_value} {self.inventory.get(next(iter(self.inventory)))}")  # Debug-Ausgabe
    return total_value
