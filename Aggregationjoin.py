import sqlite3

conn = sqlite3.connect('clients_purchases_aggregationjoin.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        client_id INTEGER PRIMARY KEY,
        client_name TEXT NOT NULL
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS purchases (
        purchase_id INTEGER PRIMARY KEY,
        client_id INTEGER,
        product_id INTEGER NOT NULL,
        FOREIGN KEY (client_id) REFERENCES clients(client_id)
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
    INSERT INTO purchases (purchase_id, client_id, product_id) 
    VALUES (?, ?, ?);
''', [
    (101, 1, 1),  
    (102, 1, 2),  
    (103, 2, 1), 
    (104, 2, 3),  
    (105, 3, 2),  
    (106, 3, 4)
])

cursor.execute("SELECT * FROM purchases")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute('''
    SELECT clients.client_name, COUNT(purchases.product_id) AS total_products_bought
    FROM clients
    JOIN purchases ON clients.client_id = purchases.client_id
    GROUP BY clients.client_name;
''')

rows = cursor.fetchall()

print("\n Client Name  | Total Products Bought")
print("------------------------------------")
for row in rows:
    client_name = row[0]
    total_products_bought = row[1]
    print(f"{client_name:<12} | {total_products_bought}")

conn.commit()
conn.close()
