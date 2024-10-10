import sqlite3

conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE accounts (account_id INTEGER PRIMARY KEY, name TEXT NOT NULL, contact_email TEXT NOT NULL);''')
cursor.execute('INSERT INTO accounts (account_id, name, contact_email) VALUES (1, "Emma", "emma@example.com");')
cursor.execute('INSERT INTO accounts (account_id, name, contact_email) VALUES (2, "Liam", "liam@example.com");')

try:
    cursor.execute('INSERT INTO accounts (account_id, name, contact_email) VALUES (3, NULL, "noah@example.com");')
except sqlite3.IntegrityError as e:
    print("Error:", e)  

try:
    cursor.execute('INSERT INTO accounts (account_id, name, contact_email) VALUES (4, "Noah", NULL);')
except sqlite3.IntegrityError as e:
    print("Error:", e) 

print("\nCurrent data in the accounts table:")
cursor.execute('SELECT * FROM accounts')
for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()
