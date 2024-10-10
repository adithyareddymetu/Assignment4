import sqlite3

connection = sqlite3.connect('CustomerProductOrders.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL
);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS products (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_name TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);''')

cursor.executemany('''INSERT INTO customers (customer_id, customer_name) VALUES (?, ?);''', [
    (1, 'Aditi'),
    (2, 'Rohan'),
    (3, 'Sneha'),
    (4, 'Vikram'),
    (5, 'Meera')
])

cursor.execute("SELECT * FROM customers")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.executemany('''INSERT INTO products (order_id, customer_id, product_name) VALUES (?, ?, ?);''', [
    (101, 1, 'Tablet'),
    (102, 2, 'Laptop'),
    (103, 1, 'Smartphone'),
    (104, 3, 'Camera'),
    (105, 4, 'Smartwatch'),
    (106, 5, 'Bluetooth Speaker'),
    (107, 3, 'Keyboard'),
    (108, 2, 'Monitor')
])

cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute('''SELECT customers.customer_name, products.product_name FROM customers
                  LEFT JOIN products ON customers.customer_id = products.customer_id;''')
rows = cursor.fetchall()
for row in rows:
    print(row)

connection.commit()
connection.close()
