import json
from .product import Product

class InventoryManager:
    def __init__(self, file_name='inventory.json'):
        self.inventory = {}
        self.file_name = file_name
        self.load_inventory()  # Beim Starten wird das Inventar geladen

    def add_product(self, product):
        """Fügen Sie ein Produkt zum Inventar hinzu."""
        if product.sku in self.inventory:
            print(f"Produkt '{product.name}' mit SKU '{product.sku}' ist bereits vorhanden.")
        else:
            self.inventory[product.sku] = product
            self.save_inventory()  # Speichern nach Hinzufügen des Produkts
            print(f"Produkt '{product.name}' zum Inventar hinzugefügt.")

    def remove_product(self, sku):
        """Entfernen Sie ein Produkt aus dem Inventar."""
        if sku in self.inventory:
            del self.inventory[sku]
            self.save_inventory()  # Speichern nach Entfernen des Produkts
            print(f"Produkt mit SKU '{sku}' aus dem Inventar entfernt.")
        else:
            print(f"Produkt mit SKU '{sku}' nicht gefunden.")

    def update_product_quantity(self, sku, new_quantity):
        """Aktualisieren Sie die Menge eines vorhandenen Produkts."""
        if sku in self.inventory:
            self.inventory[sku].update_quantity(new_quantity)
            self.save_inventory()  # Speichern nach Aktualisierung der Menge
            print(f"Produkt mit SKU '{sku}' Menge auf {new_quantity} aktualisiert.")
        else:
            print(f"Produkt mit SKU '{sku}' nicht gefunden.")

    def get_product_info(self, sku):
        """Produktinformationen nach SKU abrufen."""
        if sku in self.inventory:
            return self.inventory[sku].get_product_info()
        else:
            return f"Produkt mit SKU '{sku}' nicht gefunden."

    def get_total_inventory_value(self):
        """Berechnen Sie den Gesamtbestandswert, indem Sie die Werte aller Produkte addieren."""
        total_value = sum(product.unit_price * product.quantity for product in self.inventory.values())
        return total_value

    def search_product(self, search_term):
        """Suchen Sie nach einem Produkt anhand der SKU oder des Namens."""
        results = []
        for product in self.inventory.values():
            if search_term.lower() in product.name.lower() or search_term.lower() in product.sku.lower():
                results.append(product.get_product_info())
        if results:
            return "\n\n".join(results)
        else:
            return "Keine Produkte gefunden, die dem Suchbegriff entsprechen."

    def save_inventory(self):
        """Speichern Sie das Inventar in einer JSON-Datei."""
        with open(self.file_name, 'w') as file:
            products_data = []
            for product in self.inventory.values():
                product_data = {
                'name': product.name,
                'description': product.description, 
                'sku': product.sku,
                'quantity': product.quantity,
                'unit_price': product.unit_price,
                'purchase_price': product.purchase_price, 
                'profit_rate': product.profit_rate,  
                'currency': product.currency  
                }
                products_data.append(product_data)
            json.dump(products_data, file, indent=4)

    def load_inventory(self):
        """Laden Sie das Inventar aus der JSON-Datei."""
        try:
            with open(self.file_name, 'r') as file:
            # Überprüfen, ob die Datei leer ist
                file_content = file.read().strip()
                if not file_content:  # Falls die Datei leer ist
                    print(f"Die Datei '{self.file_name}' ist leer. Keine Produkte zum Laden.")
                    return

            # Wenn die Datei nicht leer ist, laden wir die Daten
                products_data = json.loads(file_content)
            
                for prod_data in products_data:
                    try:
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
                    except KeyError as e:
                        print(f"Fehlender Schlüssel in den Produktdaten: {e}")
                    except Exception as e:
                        print(f"Fehler beim Laden eines Produkts: {e}")

        except FileNotFoundError:
        # Wenn die Datei nicht existiert, erstellen wir eine leere Datei
            print(f"Keine vorherigen Bestandsdaten gefunden, starte neu. Erstelle '{self.file_name}'.")
            with open(self.file_name, 'w') as file:
                json.dump([], file)  # Erstelle eine leere JSON-Datei
        except json.JSONDecodeError:
            print("Fehler beim Dekodieren der JSON-Datei. Möglicherweise ist die Datei beschädigt oder enthält ungültige Daten.")
        except Exception as e:
            print(f"Unbekannter Fehler beim Laden der Datei: {e}")