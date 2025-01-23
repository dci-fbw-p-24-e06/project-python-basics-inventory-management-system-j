# Bestandsverwaltungssystem

Ziel dieses Projekts ist die Entwicklung eines einfachen Bestandsverwaltungssystems für ein Geschäft. Das System ermöglicht es Ihnen, Produkte hinzuzufügen, Produkte zu entfernen, Mengen zu aktualisieren, Produktinformationen abzurufen und den Gesamtwert des Bestands zu berechnen.
Es umfasst die Erstellung von Klassen zur Darstellung von Produkten und eines Bestandsmanagers zur Handhabung von Produktvorgängen. Sie implementieren Unit-Tests mithilfe des Unittest-Moduls und simulieren externe Abhängigkeiten zum Testen.

#### Voraussetzungen:
Grundkenntnisse in den folgenden Unterthemen:
- Zeichenfolgen
- Sammlungen
- Anweisungen und Schleifen
- Funktionen
- OOP
- Ausnahmen
- Testen
- I/O
- Module und Pakete
<br>
<br>

**Projektstruktur**

Um Ihr Projekt zu organisieren, erstellen Sie mehrere Dateien und Ordner. Folgen Sie der unten stehenden Projektstruktur, um Ihr Projekt einzurichten.

```
InventoryManagementSystem/
├── inventory/
│ ├── __init__.py
│ ├── product.py
│ └── inventory_manager.py
├── tests/
│ ├── __init__.py
│ └── test_inventory_manager.py
└── main.py
```
<br>
<br>

### Implementierungsschritte

1. Implementieren Sie die `Produktklasse` in `product.py`
- Fügen Sie der `Produkt`-Klasse Attribute Ihrer Wahl wie `Name`, `Preis`, `Menge` usw. hinzu
- Implementieren Sie Methoden zum Aktualisieren von Produktdetails wie `update_quantity`, um die Menge des Produkts zu aktualisieren. Sie können ähnliche Methoden zum Aktualisieren des Preises oder anderer notwendiger Attribute implementieren.
- Implementieren Sie die Methode `get_product_info` (oder nennen Sie sie, wie Sie möchten), um eine Zeichenfolgendarstellung der Produktinformationen zurückzugeben.

2. Implementieren Sie die Klasse `InventoryManager` in `inventory_manager.py`:
- Definieren Sie eine Klasse namens `InventoryManager`.
- Implementieren Sie Methoden in der Klasse, um Produkte hinzuzufügen, Produkte zu entfernen und Mengen zu aktualisieren
- Erstellen Sie eine Methode zum Abrufen von Produktinformationen, indem Sie einen `product_name`-Parameter angeben. Wenn das Produkt mit dem angegebenen Namen im Inventar vorhanden ist, rufen Sie die entsprechende Methode des `Product`-Objekts auf, um seine Informationen abzurufen; andernfalls geben Sie die Meldung „Produkt nicht gefunden“ zurück.
- Implementieren Sie eine Methode namens `get_total_inventory_value`, um den Gesamtwert des gesamten Inventars zu berechnen. Mit dieser Methode können Sie den Gesamtwert des Inventars ermitteln, indem Sie die Einzelwerte jedes Produkts basierend auf seinem Preis und seiner Menge addieren.

3. Denken Sie daran, die Datei `main.py` auf der Stammebene zu erstellen.
- Es dient als Einstiegspunkt für Ihre Anwendung. Normalerweise ist die Hauptdatei für das Starten des Programms, das Initialisieren von Objekten und das Aufrufen relevanter Funktionen verantwortlich.
- Erstellt eine Instanz des „InventoryManager“, fügt dem Inventar einige Beispielprodukte hinzu und berechnet und druckt dann den Gesamtinventarwert.

4. Schreiben Sie Unit-Tests in „test_inventory_manager.py“:
- Verwenden Sie das Modul unittest, um Unit-Tests für die Klassen „Product“ und „InventoryManager“ zu schreiben.
- Importieren Sie alle erforderlichen Module in die Testdatei.
- Erstellen Sie in der Methode „setUp“ eine Instanz der Klasse „InventoryManager“ und weisen Sie sie „self.inventory_manager“ zu. Diese Methode wird vor jeder Testmethode ausgeführt.
- Definieren Sie innerhalb der Klasse „TestInventoryManager“ Testmethoden für jede Funktion der Klasse „InventoryManager“. (z. B. die Methode zum Hinzufügen, Entfernen und so weiter von Produkten;

Denken Sie an die Phase „Anordnen, Ausführen und Bestätigen“. Jede Testmethode sollte mit den erforderlichen Vorkehrungen beginnen, z. B. dem Erstellen von „Produkt“-Instanzen und dem Hinzufügen dieser zum „InventoryManager“.)

- Navigieren Sie zum Stammordner Ihres Projekts („InventoryManagementSystem“).

- Führen Sie den folgenden Befehl aus, um die Unit-Tests auszuführen: „python3 -m unittest“.

5. Zusätzliche Funktionen hinzufügen (optional):

- Sie können das Projekt erweitern, indem Sie den Klassen „Produkt“ und „InventoryManager“ zusätzliche Funktionen hinzufügen.

Sie können beispielsweise Funktionen wie das Suchen nach Produkten, das Erstellen von Berichten oder Statistiken zum Inventar usw. implementieren.

- Schreiben Sie entsprechende Unit-Tests für die neuen Funktionen, um deren Richtigkeit sicherzustellen.

- Aktualisieren Sie die Testfälle in „test_inventory_manager.py“, um die neuen Funktionen abzudecken.

- **Hinweis**
- Sie können alle externen Abhängigkeiten oder Interaktionen als externe Dienste **simulieren**, indem Sie das Modul „mock“ verwenden, um die Tests zu isolieren.

Identifizieren Sie den Teil des Codes, der zu Testzwecken simuliert werden muss (z. B. das Verhalten der `Product`-Objekte und des `InventoryManager`-Objekts in `get_total_inventory_value`).
Ich kann jedoch zum besseren Verständnis vorschlagen, eine Funktion mit externen Abhängigkeiten in der `InventoryManager`-Klasse hinzuzufügen:
- Sie können eine `external_service.py`-Datei im Inventarordner erstellen. Erstellen Sie eine Methode (`add_product_with_logging`), die den Namen des Produkts als Argument verwendet und eine Meldung ausgibt, um den Protokollierungsprozess zu simulieren („Logging product added:“).
(Denken Sie daran, dass dies ein vereinfachtes Beispiel zur Veranschaulichung ist das Konzept einer externen Abhängigkeit. In einem realen Szenario könnte die Klasse „ExternalService“ mit einer Datenbank, API oder anderen externen Systemen interagieren.)
- Die Klasse „ExternalService“ simuliert einen externen Dienst, wie z. B. eine Protokollierungs- oder Benachrichtigungsfunktion, in „inventory_manager.py“ (Rufen Sie den externen Dienst auf, um das Hinzufügen des Produkts zu protokollieren)
- Verwenden Sie Mocking, um „add_product_with_logging“ und „get_total_inventory_value“ zu testen.

(Sie können sich dieses Video ansehen, um einen Eindruck zu bekommen: https://www.youtube.com/watch?v=xT4SV7AH3G8 (bitte keine Sorge, in Zukunft werden wir mehr über API lernen)

Denken Sie daran, sauberen und lesbaren Code zu schreiben, Best Practices zu befolgen und Ihren Code mit Kommentaren zu dokumentieren, um ihn für Sie selbst und andere, die ihn in Zukunft überprüfen oder warten, verständlicher zu machen.

Durch das Abschließen dieser Übung sammeln Sie praktische Erfahrung bei der Implementierung von Unit-Tests mit unittest und der Anwendung von Mocking-Techniken zum Isolieren von Abhängigkeiten für Tests.

Sie verbessern außerdem Ihr Verständnis für das Schreiben von Testfällen, Behauptungen und das Überprüfen erwarteter Ergebnisse.