import sqlite3

conn = sqlite3.connect('existing_table_check_constraint.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE staff (staff_id INTEGER PRIMARY KEY, staff_name TEXT NOT NULL, salary REAL NOT NULL CHECK (salary > 0));''')

cursor.execute('''INSERT INTO staff (staff_id, staff_name, salary) VALUES (101, 'Riya', 12000);''')
cursor.execute('''INSERT INTO staff (staff_id, staff_name, salary) VALUES (201, 'Kiran', 14000);''')

conn.commit()
conn.close()
