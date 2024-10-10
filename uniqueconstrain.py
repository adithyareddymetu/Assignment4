import sqlite3

conn = sqlite3.connect('user_management.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE accounts (account_id INTEGER PRIMARY KEY, account_name TEXT NOT NULL, email TEXT NOT NULL UNIQUE);''')
cursor.execute('''INSERT INTO accounts (account_id, account_name, email) VALUES (1, 'Alice Brown', 'alice.brown@example.com');''')
cursor.execute('''INSERT INTO accounts (account_id, account_name, email) VALUES (2, 'Bob White', 'bob.white@example.com');''')

cursor.execute('''SELECT * FROM accounts;''')
print(cursor.fetchall())

cursor.execute('''INSERT INTO accounts (account_id, account_name, email) VALUES (3, 'Charlie Green', 'alice.brown@example.com');''')

conn.commit()
conn.close()
