import sqlite3

conn = sqlite3.connect('inventory_management.db')
cursor = conn.cursor()

cursor.execute('PRAGMA foreign_keys = ON;')

cursor.execute(''' 
    CREATE TABLE item_categories (
        category_id INTEGER PRIMARY KEY,
        category_name TEXT NOT NULL)
''')

cursor.execute(''' 
    CREATE TABLE items (
        item_id INTEGER PRIMARY KEY,
        item_name TEXT NOT NULL,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES item_categories(category_id) ON DELETE CASCADE)
''')

categories = [(1, 'Electronics'), (2, 'Apparel'), (3, 'Literature')]
cursor.executemany('INSERT INTO item_categories (category_id, category_name) VALUES (?, ?)', categories)

items = [
    (1, 'Smartphone', 1),
    (2, 'Laptop', 1),
    (3, 'T-shirt', 2),
    (4, 'Novel', 3)
]

cursor.executemany('INSERT INTO items (item_id, item_name, category_id) VALUES (?, ?, ?)', items)

print("Initial data in item_categories table:")
cursor.execute('SELECT * FROM item_categories')
print(cursor.fetchall())

print("\nInitial data in items table:")
cursor.execute('SELECT * FROM items')
print(cursor.fetchall())

cursor.execute('DELETE FROM item_categories WHERE category_id = 1')

print("\nData in item_categories table after deleting category_id = 1 (Electronics):")
cursor.execute('SELECT * FROM item_categories')
print(cursor.fetchall())

print("\nData in items table after deleting category_id = 1 (Electronics):")
cursor.execute('SELECT * FROM items')
print(cursor.fetchall())

conn.commit()
conn.close()
