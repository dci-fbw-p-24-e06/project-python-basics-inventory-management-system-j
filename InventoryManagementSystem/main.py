from inventory.product import Items


def total_prices():
    total_items_price = 0
    for item in Items:
        price_to_use = item['purchasePrice'] if 'purchasePrice' in item else item['unitPrice']
        total_items_price += item['quantity'] * price_to_use
    
result = total_prices()

#total_items_value = total_items_price
print(f'Total value of all available products: {result} EUR')