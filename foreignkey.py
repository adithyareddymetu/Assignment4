import sqlite3

conn = sqlite3.connect('enrollment_system.db')
cursor = conn.cursor()
cursor.execute('PRAGMA foreign_keys = ON;')

cursor.execute('''CREATE TABLE learners (learner_id INTEGER PRIMARY KEY, learner_name TEXT NOT NULL);''')
cursor.execute('''CREATE TABLE classes (class_id INTEGER, class_name TEXT NOT NULL, department_id INTEGER, PRIMARY KEY (class_id, department_id)); ''')
cursor.execute('''CREATE TABLE enrollment (
    learner_id INTEGER,
    class_id INTEGER,
    department_id INTEGER,
    FOREIGN KEY (learner_id) REFERENCES learners(learner_id) ON DELETE CASCADE,
    FOREIGN KEY (class_id, department_id) REFERENCES classes(class_id, department_id) ON DELETE CASCADE,
    PRIMARY KEY (learner_id, class_id, department_id));''')

cursor.execute('INSERT INTO learners (learner_id, learner_name) VALUES (1, "Eve");')
cursor.execute('INSERT INTO learners (learner_id, learner_name) VALUES (2, "Frank");')
cursor.execute('INSERT INTO classes (class_id, class_name, department_id) VALUES (201, "Web Development", 1);')
cursor.execute('INSERT INTO classes (class_id, class_name, department_id) VALUES (202, "Data Structures", 1);')
cursor.execute('INSERT INTO enrollment (learner_id, class_id, department_id) VALUES (1, 201, 1);')
cursor.execute('INSERT INTO enrollment (learner_id, class_id, department_id) VALUES (2, 202, 1);')

print("\nCurrent data in the enrollment table:")
cursor.execute('SELECT * FROM enrollment')
for row in cursor.fetchall():
    print(row)

cursor.execute('INSERT INTO enrollment (learner_id, class_id, department_id) VALUES (3, 201, 1);')
cursor.execute('INSERT INTO enrollment (learner_id, class_id, department_id) VALUES (1, 203, 1);')

conn.commit()
conn.close()
