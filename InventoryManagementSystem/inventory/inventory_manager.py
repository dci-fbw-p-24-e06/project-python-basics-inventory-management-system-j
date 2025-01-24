from product import Items

class InventoryManager:
    def find_product(self, items):
        
        product_name = input('Enter the name of the product you want to find: ')
        for item in items: 
            if item['name'] == product_name:
                return item  
        return "Sold out"

inventory_manager = InventoryManager()

result = inventory_manager.find_product(Items)

if result != "Sorry, Sold out":
    print(f"Product found: {result}")
else:
    print(result)  


def get_total_inventory_value(items):
    total_items_price = 0
    for item in Items:
        price_to_use = item['purchasePrice'] if 'purchasePrice' in item else item['unitPrice']
        total_items_price += item['quantity'] * price_to_use
    
    return total_items_price

total_items_value = get_total_inventory_value(Items)
print(f'Total value of all available products: {total_items_value} EUR')