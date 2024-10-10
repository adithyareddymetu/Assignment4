import sqlite3

conn = sqlite3.connect('composite_key_constraint.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE learners (learner_id INTEGER PRIMARY KEY, learner_name TEXT NOT NULL);''')
cursor.execute('''CREATE TABLE subjects (subject_id INTEGER PRIMARY KEY, subject_name TEXT NOT NULL);''')
cursor.execute('''CREATE TABLE learner_subjects (
    learner_id INTEGER, subject_id INTEGER, PRIMARY KEY (learner_id, subject_id), FOREIGN KEY (learner_id) REFERENCES learners(learner_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id));''')
cursor.execute('INSERT INTO learners (learner_id, learner_name) VALUES (1, "John");')
cursor.execute('INSERT INTO learners (learner_id, learner_name) VALUES (2, "Emily");')
cursor.execute('INSERT INTO subjects (subject_id, subject_name) VALUES (101, "Biology");')
cursor.execute('INSERT INTO subjects (subject_id, subject_name) VALUES (102, "Chemistry");')
cursor.execute('INSERT INTO learner_subjects (learner_id, subject_id) VALUES (1, 101);')
cursor.execute('INSERT INTO learner_subjects (learner_id, subject_id) VALUES (2, 102);')

print("\n Current data in the learner_subjects table:")
cursor.execute('SELECT * FROM learner_subjects')
for row in cursor.fetchall():
    print(row)

try:
    cursor.execute('INSERT INTO learner_subjects (learner_id, subject_id) VALUES (1, 101);') 
except sqlite3.IntegrityError as e:
    print("Error:", e) 

cursor.execute('INSERT INTO learner_subjects (learner_id, subject_id) VALUES (1, 102);')
conn.commit()
conn.close()
