import sqlite3

conn = sqlite3.connect('client_purchases_multiplejoin.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE clients (
        client_id INTEGER PRIMARY KEY,
        client_name TEXT NOT NULL
    );
''')

cursor.execute('''
    CREATE TABLE products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT NOT NULL
    );
''')

cursor.execute('''
    CREATE TABLE purchases (
        purchase_id INTEGER PRIMARY KEY,
        client_id INTEGER,
        product_id INTEGER,
        purchase_date TEXT NOT NULL,
        FOREIGN KEY (client_id) REFERENCES clients(client_id),
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    );
''')

cursor.executemany('''
    INSERT INTO clients (client_id, client_name) 
    VALUES (?, ?);
''', [
    (1, 'Liam Davis'),
    (2, 'Emma White'),
    (3, 'Noah Evans')
])

cursor.execute("SELECT * FROM clients")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.executemany('''
    INSERT INTO products (product_id, product_name) 
    VALUES (?, ?);
''', [
    (1, 'Laptop'),
    (2, 'Smartphone'),
    (3, 'Tablet'),
    (4, 'Camera')
])

cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.executemany('''
    INSERT INTO purchases (purchase_id, client_id, product_id, purchase_date) 
    VALUES (?, ?, ?, ?);
''', [
    (101, 1, 1, '2024-01-15'),
    (102, 1, 2, '2024-01-20'),
    (103, 2, 3, '2024-02-05'),
    (104, 3, 4, '2024-02-10')
])

cursor.execute("SELECT * FROM purchases")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute('''
    SELECT clients.client_name, products.product_name, purchases.purchase_date
    FROM purchases
    JOIN clients ON purchases.client_id = clients.client_id
    JOIN products ON purchases.product_id = products.product_id;
''')

rows = cursor.fetchall()

print("Client Name    | Product Name  | Purchase Date")
print("---------------------------------------------")
for row in rows:
    client_name = row[0]
    product_name = row[1]
    purchase_date = row[2]
    print(f"{client_name:<14} | {product_name:<12} | {purchase_date}")

conn.commit()
conn.close()
