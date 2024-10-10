import sqlite3
connection = sqlite3.connect('CustomerOrders.db')
cursor = connection.cursor()
# creating table for customers
cursor.execute('''CREATE TABLE IF NOT EXISTS customers ( customer_id INTEGER PRIMARY KEY,customer_name TEXT NOT NULL);''')
# creating table for orders
cursor.execute('''CREATE TABLE IF NOT EXISTS orders ( order_id INTEGER PRIMARY KEY,customer_id INTEGER,
               product_name TEXT NOT NULL,FOREIGN KEY (customer_id) REFERENCES customers(customer_id));''')
# inserting records into customer table 
cursor.executemany('''INSERT INTO customers (customer_id, customer_name) VALUES (?, ?);''', [
    (1, 'Adi'),
    (2, 'Suresh'),
    (3, 'Mani'),
    (4, 'Venkat'),
    (5, 'Janu')
])
# selecting the records from customers table
cursor.execute("Select *from customers")
print("\n Customers Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row)
# inserting records into the orders table
cursor.executemany('''
    INSERT INTO orders (order_id, customer_id, product_name) VALUES (?, ?, ?);''', [
    (101, 1, 'Laptop'),
    (102, 2, 'Mixer'),
    (103, 1, 'Headphones'),
    (104, 3, 'Tablet'),
    (105, 4, 'Grinder'),
    (106, 5, 'Camera'),
    (107, 3, 'watch'),
    (108, 2, 'Headset')
])
#selecting the records from orders table
cursor.execute("Select *from orders")
print("\n Orders Table \n")
rows = cursor.fetchall()
for row in rows:
    print(row)

# performing inner join between customer and order table
cursor.execute('''SELECT customers.customer_name, orders.product_name FROM customers 
               INNER JOIN orders ON customers.customer_id = orders.customer_id;''')
print("\n Inner Join \n")
rows = cursor.fetchall()
for row in rows:
    print(row)
connection.commit()
connection.close()