import json
import os
from .product import Product

class InventoryManager:
    def __init__(self, file_name=os.path.join("..", "inventory.json")):
        self.inventory = {}
        self.file_name = file_name
        print(f"Inventory file path set to: {self.file_name}")
        print(f"Absolute path: {os.path.abspath(self.file_name)}")
        self.load_inventory()

    # Der Rest der Klasse bleibt unverändert
    def add_product(self, product):
        """Add a product to the inventory."""
        if product.sku in self.inventory:
            print(f"Product '{product.name}' with SKU '{product.sku}' already exists.")
        else:
            self.inventory[product.sku] = product
            self.save_inventory()
            print(f"Product '{product.name}' added to inventory.")

    def remove_product(self, sku):
        """Remove a product from the inventory."""
        if sku in self.inventory:
            del self.inventory[sku]
            self.save_inventory()
            print(f"Product with SKU '{sku}' removed from inventory.")
        else:
            print(f"Product with SKU '{sku}' not found.")

    def update_product_quantity(self, sku, new_quantity):
        """Update the quantity of an existing product."""
        if sku in self.inventory:
            if self.inventory[sku].update_quantity(new_quantity):
                self.save_inventory()
                print(f"Quantity updated for SKU '{sku}' to {new_quantity}")
        else:
            print(f"Product with SKU '{sku}' not found.")

    def get_product_info(self, sku):
        """Get product information by SKU."""
        if sku in self.inventory:
            return self.inventory[sku].get_product_info()
        return f"Product with SKU '{sku}' not found."

    def get_total_inventory_value(self):
        """Calculate the total inventory value."""
        if not self.inventory:
            print("Inventory is empty")
            return 0.0
        total = sum(product.unit_price * product.quantity for product in self.inventory.values())
        print(f"Calculated total value: {total}")
        return total

    def search_product(self, search_term):
        """Search for a product by SKU or name."""
        results = []
        for product in self.inventory.values():
            if (search_term.lower() in product.name.lower() or 
                search_term.lower() in product.sku.lower()):
                results.append(product.get_product_info())
        if results:
            return "\n\n".join(results)
        return "No products found matching the search term."

    def save_inventory(self):
        """Save the inventory to a JSON file."""
        try:
            with open(self.file_name, 'w', encoding='utf-8') as file:
                products_data = [{
                    'name': product.name,
                    'description': product.description,
                    'sku': product.sku,
                    'quantity': product.quantity,
                    'unit_price': product.unit_price,
                    'purchase_price': product.purchase_price,
                    'profit_rate': product.profit_rate,
                    'currency': product.currency
                } for product in self.inventory.values()]
                json.dump(products_data, file, indent=4)
            print(f"Inventory saved to {self.file_name}")
        except Exception as e:
            print(f"Error saving inventory: {e}")

    def load_inventory(self):
        """Load the inventory from the JSON file."""
        try:
            if not os.path.exists(self.file_name):
                print(f"File '{self.file_name}' not found, starting with empty inventory")
                return

            with open(self.file_name, 'r', encoding='utf-8') as file:
                content = file.read().strip()
                if not content:
                    print(f"File '{self.file_name}' is empty")
                    return

                products_data = json.loads(content)
                self.inventory.clear()
                for prod_data in products_data:
                    product = Product(
                        prod_data['name'],
                        prod_data['description'],
                        prod_data['sku'],
                        prod_data['quantity'],
                        prod_data['unit_price'],
                        prod_data['purchase_price'],
                        prod_data['profit_rate'],
                        prod_data['currency']
                    )
                    self.inventory[product.sku] = product
                print(f"Loaded {len(products_data)} products from file")

        except json.JSONDecodeError:
            print("Error: Invalid JSON format in inventory file")
        except Exception as e:
            print(f"Error loading inventory: {e}")