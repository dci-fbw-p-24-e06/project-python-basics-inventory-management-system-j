from inventory.product import Items
from inventory.inventory_manager import get_total_inventory_value

def total_prices():
    total_items_price = 0
    for item in Items:
        price_to_use = item['purchasePrice'] if 'purchasePrice' in item else item['unitPrice']
        total_items_price += item['quantity'] * price_to_use
    
    return total_items_price

total_items_value = get_total_inventory_value(Items)
print(f'Total value of all available products: {total_items_value} EUR')