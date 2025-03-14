import os
import sys
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

def print_submenu_4_6(info):
    print(f"\n{info}")
    print("\nSubmenu:")
    print("1. Product ändern")
    print("2. Back (zurück zum Hauptmenü)")

def print_submenu_5(result):
    print(f"\n{result}")
    print("\nSubmenu:")
    print("1. Back (zurück zum Hauptmenü)")

def update_product(inventory_manager):
    try:
        sku = input("Enter the SKU of the product to update: ").strip()
        if sku in inventory_manager.inventory:
            print(f"\nUpdating product with SKU {sku}")
            print("What would you like to update?")
            print("1. Quantity")
            print("2. Unit Price")
            print("3. Back (zurück zum Hauptmenü)")
            
            choice = input("Enter your choice: ").strip()
            
            if choice == '1':
                new_quantity = int(input("Enter new quantity: "))
                inventory_manager.update_product_quantity(sku, new_quantity)
                print(f"Quantity for SKU {sku} updated to {new_quantity}")
            elif choice == '2':
                new_price = float(input("Enter new unit price: "))
                if inventory_manager.inventory[sku].update_price(new_price):
                    inventory_manager.save_inventory()
                    print(f"Unit price for SKU {sku} updated to {new_price}")
            elif choice == '3':
                return
            else:
                print("Invalid choice. Returning to main menu.")
        else:
            print(f"Product with SKU '{sku}' not found.")
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    try:
        # Lasse den Standardpfad aus InventoryManager greifen
        inventory_manager = InventoryManager()
    except Exception as e:
        print(f"Failed to initialize InventoryManager: {e}")
        sys.exit(1)

    main_loop = True
    while main_loop:
        print_menu()
        choice = input("Enter your choice: ").strip()

        try:
            if choice == '1':
                name = input("Enter product name: ").strip()
                description = input("Enter product description: ").strip()
                sku = input("Enter product SKU: ").strip()
                quantity = int(input("Enter product quantity: "))
                unit_price = float(input("Enter product unit price: "))
                purchase_price = float(input("Enter product purchase price: "))
                profit_rate = float(input("Enter product profit rate: "))
                currency = input("Enter product currency: ").strip()

                product = Product(name, description, sku, quantity, unit_price, purchase_price, profit_rate, currency)
                inventory_manager.add_product(product)

            elif choice == '2':
                sku = input("Enter SKU of the product to remove: ").strip()
                inventory_manager.remove_product(sku)

            elif choice == '3':
                sku = input("Enter SKU of the product to update quantity: ").strip()
                new_quantity = int(input("Enter new quantity: "))
                inventory_manager.update_product_quantity(sku, new_quantity)

            elif choice == '4':
                sku = input("Enter SKU of the product to get info: ").strip()
                info = inventory_manager.get_product_info(sku)
                if info and isinstance(info, str):
                    print_submenu_4_6(info)
                    submenu_loop = True
                    while submenu_loop:
                        try:
                            sub_choice = input("Enter your choice: ").strip()
                            if sub_choice == '1':
                                update_product(inventory_manager)
                                info = inventory_manager.get_product_info(sku)
                                print_submenu_4_6(info)
                            elif sub_choice == '2':
                                submenu_loop = False
                            else:
                                print("Invalid choice. Please try again.")
                        except Exception as e:
                            print(f"Error in submenu: {e}")
                            print("Returning to submenu loop...")
                else:
                    print("No product found or invalid SKU.")

            elif choice == '5':
                total_value = inventory_manager.get_total_inventory_value()
                currency = inventory_manager.inventory[list(inventory_manager.inventory.keys())[0]].currency if inventory_manager.inventory else 'EUR'
                result = f"Total Inventory Value: {total_value:.2f} {currency}"
                print_submenu_5(result)
                submenu_loop = True
                while submenu_loop:
                    try:
                        sub_choice = input("Enter your choice: ").strip()
                        if sub_choice == '1':
                            submenu_loop = False
                        else:
                            print("Invalid choice. Please try again.")
                    except Exception as e:
                        print(f"Error in submenu: {e}")
                        print("Returning to submenu loop...")

            elif choice == '6':
                search_term = input("Enter product name or SKU to search: ").strip()
                results = inventory_manager.search_product(search_term)
                if results and isinstance(results, str) and results.strip():
                    product_infos = results.split("\n\n")
                    submenu_loop = True
                    for info in product_infos:
                        if submenu_loop and "SKU:" in info:
                            print_submenu_4_6(info)
                            try:
                                sub_choice = input("Enter your choice for this product: ").strip()
                                if sub_choice == '1':
                                    update_product(inventory_manager)
                                    updated_results = inventory_manager.search_product(search_term)
                                    if updated_results and isinstance(updated_results, str):
                                        product_infos = updated_results.split("\n\n")
                                elif sub_choice == '2':
                                    submenu_loop = False
                                    break
                                else:
                                    print("Invalid choice. Please try again.")
                            except Exception as e:
                                print(f"Error in submenu: {e}")
                                print("Returning to submenu loop...")
                else:
                    print("No products found matching the search term.")

            elif choice == '7':
                print("Exiting program.")
                main_loop = False
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")
        except KeyError as e:
            print(f"Key error occurred: {e}. Check if the SKU or data exists.")
        except AttributeError as e:
            print(f"Attribute error occurred: {e}. Check inventory data.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Returning to menu...")

if __name__ == "__main__":
    main()