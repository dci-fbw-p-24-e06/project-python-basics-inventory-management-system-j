# main.py

from inventory.product import Product
from inventory.inventory_manager import InventoryManager

def print_menu():
    print("\nMenu:")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Update Product Quantity")
    print("4. Get Product Info")
    print("5. Get Total Inventory Value")
    print("6. Search Product")
    print("7. Exit")

def main():
    inventory_manager = InventoryManager()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter product name: ")
            description = input("Enter product description: ")
            sku = input("Enter product SKU: ")
            quantity = int(input("Enter product quantity: "))
            unit_price = float(input("Enter product unit price: "))
            purchase_price = float(input("Enter product purchase price: "))
            profit_rate = float(input("Enter product profit rate: "))
            currency = input("Enter product currency: ")

            product = Product(name, description, sku, quantity, unit_price, purchase_price, profit_rate, currency)
            inventory_manager.add_product(product)

        elif choice == '2':
            sku = input("Enter SKU of the product to remove: ")
            inventory_manager.remove_product(sku)

        elif choice == '3':
            sku = input("Enter SKU of the product to update quantity: ")
            new_quantity = int(input("Enter new quantity: "))
            inventory_manager.update_product_quantity(sku, new_quantity)

        elif choice == '4':
            sku = input("Enter SKU of the product to get info: ")
            print(inventory_manager.get_product_info(sku))

        elif choice == '5':
            total_value = inventory_manager.get_total_inventory_value()
            print(f"Total Inventory Value: {total_value} EUR")

        elif choice == '6':
            search_term = input("Enter product name or SKU to search: ")
            print(inventory_manager.search_product(search_term))

        elif choice == '7':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()