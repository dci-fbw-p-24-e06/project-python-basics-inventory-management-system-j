# inventory/inventory_manager.py

from .product import Product

class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product):
        """Add a product to the inventory."""
        if product.sku in self.inventory:
            print(f"Product '{product.name}' with SKU '{product.sku}' already exists.")
        else:
            self.inventory[product.sku] = product
            print(f"Product '{product.name}' added to inventory.")

    def remove_product(self, sku):
        """Remove a product from the inventory."""
        if sku in self.inventory:
            del self.inventory[sku]
            print(f"Product with SKU '{sku}' removed from inventory.")
        else:
            print(f"Product with SKU '{sku}' not found.")

    def update_product_quantity(self, sku, new_quantity):
        """Update the quantity of an existing product."""
        if sku in self.inventory:
            self.inventory[sku].update_quantity(new_quantity)
            print(f"Product with SKU '{sku}' quantity updated to {new_quantity}.")
        else:
            print(f"Product with SKU '{sku}' not found.")

    def get_product_info(self, sku):
        """Retrieve product information by SKU."""
        if sku in self.inventory:
            return self.inventory[sku].get_product_info()
        else:
            return f"Product with SKU '{sku}' not found."

    def get_total_inventory_value(self):
        """Calculate the total inventory value by summing up all products' values."""
        total_value = sum(product.unit_price * product.quantity for product in self.inventory.values())
        return total_value

    def search_product(self, search_term):
        """Search for a product by SKU or name."""
        results = []
        for product in self.inventory.values():
            if search_term.lower() in product.name.lower() or search_term.lower() in product.sku.lower():
                results.append(product.get_product_info())
        if results:
            return "\n\n".join(results)
        else:
            return "No products found matching your search."
