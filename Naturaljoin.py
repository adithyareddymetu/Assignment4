import sqlite3

conn = sqlite3.connect('clients_purchases_naturaljoin.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE clients (
        client_id INTEGER PRIMARY KEY,
        client_name TEXT NOT NULL
    );
''')

cursor.execute('''
    CREATE TABLE purchases (
        purchase_id INTEGER PRIMARY KEY,
        client_id INTEGER,
        purchase_date TEXT NOT NULL,
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
    INSERT INTO purchases (purchase_id, client_id, purchase_date) 
    VALUES (?, ?, ?);
''', [
    (101, 1, '2024-01-15'),  
    (102, 2, '2024-01-20'),  
    (103, 1, '2024-02-05'),  
    (104, 3, '2024-02-10')   
])

cursor.execute("SELECT * FROM purchases")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute('''
    SELECT * 
    FROM clients
    NATURAL JOIN purchases;
''')

print("\n Natural Join \n")
rows = cursor.fetchall()
print("Client Name   | Purchase ID | Purchase Date")
print("------------------------------------------")
for row in rows:
    client_name = row[1]
    purchase_id = row[2]
    purchase_date = row[3]
    print(f"{client_name:<13} | {purchase_id:<10} | {purchase_date}")

conn.commit()
conn.close()
