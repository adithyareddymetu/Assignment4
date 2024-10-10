import sqlite3

conn = sqlite3.connect('items_clients_crossjoin.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE items (
        item_id INTEGER PRIMARY KEY,
        item_name TEXT NOT NULL
    );
''')

cursor.execute('''
    CREATE TABLE clients (
        client_id INTEGER PRIMARY KEY,
        client_name TEXT NOT NULL
    );
''')

cursor.executemany('''
    INSERT INTO items (item_id, item_name) 
    VALUES (?, ?);
''', [
    (1, 'Phone'),
    (2, 'Headphones'),
    (3, 'Charger'),
    (4, 'Monitor')
])

cursor.execute("SELECT * FROM items")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.executemany('''
    INSERT INTO clients (client_id, client_name) 
    VALUES (?, ?);
''', [
    (1, 'Liam Davis'),
    (2, 'Emma White'),
    (3, 'Noah Evans'),
    (4, 'Mia Clark')
])

cursor.execute("SELECT * FROM clients")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute('''
    SELECT items.item_name, clients.client_name
    FROM items
    CROSS JOIN clients;
''')

print("Cross Join \n")
print("Item Name    | Client Name")
print("----------------------------")
rows = cursor.fetchall()
for row in rows:
    item_name = row[0]
    client_name = row[1]
    print(f"{item_name:<12} | {client_name}")

conn.commit()
conn.close()
