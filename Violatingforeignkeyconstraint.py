import sqlite3

conn = sqlite3.connect('order_management.db')
cursor = conn.cursor()

cursor.execute('PRAGMA foreign_keys = ON;')

cursor.execute('''CREATE TABLE clients (client_id INTEGER PRIMARY KEY, client_name TEXT NOT NULL);''')
cursor.execute('''CREATE TABLE purchases (purchase_id INTEGER PRIMARY KEY, client_id INTEGER, order_date TEXT, FOREIGN KEY (client_id) REFERENCES clients(client_id));''')

cursor.execute('''INSERT INTO clients (client_id, client_name) VALUES (1, 'Alice Smith');''')
cursor.execute('''INSERT INTO clients (client_id, client_name) VALUES (2, 'Bob Johnson');''')
cursor.execute('''SELECT * FROM clients;''')
print(cursor.fetchall())

cursor.execute('''INSERT INTO purchases (purchase_id, client_id, order_date) VALUES (1, 5, '2024-10-09');''')  
cursor.execute('''SELECT * FROM purchases;''')
print(cursor.fetchall())

conn.commit()
conn.close()
