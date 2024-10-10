import sqlite3

conn = sqlite3.connect('product_validation.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE items (item_id INTEGER PRIMARY KEY, item_name TEXT NOT NULL, cost REAL NOT NULL CHECK (cost > 0));''')

cursor.execute('''INSERT INTO items (item_id, item_name, cost) VALUES (1, 'Gaming Laptop', 1200.00);''')
cursor.execute('''INSERT INTO items (item_id, item_name, cost) VALUES (2, 'Fitness Tracker', 50.00);''')

cursor.execute('''SELECT * FROM items;''')
print(cursor.fetchall())

cursor.execute('''INSERT INTO items (item_id, item_name, cost) VALUES (3, 'Basic Tracker', 0);''')

conn.commit()
conn.close()
