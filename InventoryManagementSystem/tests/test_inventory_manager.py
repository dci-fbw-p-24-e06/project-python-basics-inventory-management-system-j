import unittest
from inventory.product import Product
from inventory.inventory_manager import InventoryManager

class TestInventoryManager(unittest.TestCase):

    def setUp(self):
        self.inventory_manager = InventoryManager()

    def test_add_product(self):
        product = Product("Laptop", "Description", "SKU123", 10, 1000, 800, 20, "EUR")
        self.inventory_manager.add_product(product)
        self.assertEqual(len(self.inventory_manager.inventory), 1)

    def test_remove_product(self):
        product = Product("Laptop", "Description", "SKU123", 10, 1000, 800, 20, "EUR")
        self.inventory_manager.add_product(product)
        self.inventory_manager.remove_product("SKU123")
        self.assertEqual(len(self.inventory_manager.inventory), 0)

    def test_get_product_info(self):
        product = Product("Laptop", "Description", "SKU123", 10, 1000, 800, 20, "EUR")
        self.inventory_manager.add_product(product)
        product_info = self.inventory_manager.get_product_info("SKU123")
        self.assertIn("Name: Laptop", product_info)

    def test_total_inventory_value(self):
        product1 = Product("Laptop", "Description", "SKU123", 10, 1000, 800, 20, "EUR")
        product2 = Product("Phone", "Description", "SKU124", 5, 500, 400, 25, "EUR")
        self.inventory_manager.add_product(product1)
        self.inventory_manager.add_product(product2)
        total_value = self.inventory_manager.get_total_inventory_value()
        self.assertEqual(total_value, 10000 + 2500)

if __name__ == "__main__":
    unittest.main()