import sqlite3

conn = sqlite3.connect('course_management.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE classes (class_id INTEGER, class_name TEXT NOT NULL, faculty_id INTEGER, PRIMARY KEY (class_id, faculty_id));''')

cursor.execute('''INSERT INTO classes (class_id, class_name, faculty_id) VALUES (201, 'Intro to Programming', 1);''')
cursor.execute('''INSERT INTO classes (class_id, class_name, faculty_id) VALUES (201, 'Intro to Programming', 2);''')

try:
    cursor.execute('''INSERT INTO classes (class_id, class_name, faculty_id) VALUES (201, 'Advanced Programming', 1);''')
except sqlite3.IntegrityError as e:
    print("Error:", e)

print("\nCurrent data in the classes table:")
cursor.execute('SELECT * FROM classes')
for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()
