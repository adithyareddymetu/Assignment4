import sqlite3

conn = sqlite3.connect('staff_divisions_fullouterjoin.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE staff (
        staff_id INTEGER PRIMARY KEY,
        staff_name TEXT NOT NULL,
        division_id INTEGER,
        FOREIGN KEY (division_id) REFERENCES divisions(division_id)
    );
''')

cursor.execute('''
    CREATE TABLE divisions (
        division_id INTEGER PRIMARY KEY,
        division_name TEXT NOT NULL
    );
''')

cursor.executemany('''
    INSERT INTO divisions (division_id, division_name) 
    VALUES (?, ?);
''', [
    (1, 'Finance'),
    (2, 'Operations'),
    (3, 'Design'),
    (4, 'Development')
])

cursor.execute("SELECT * FROM divisions")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.executemany('''
    INSERT INTO staff (staff_id, staff_name, division_id) 
    VALUES (?, ?, ?);
''', [
    (1, 'Mia Clark', 1),      
    (2, 'Liam Davis', 2),     
    (3, 'Noah Evans', None),  
    (4, 'Emma White', 3)      
])

cursor.execute("SELECT * FROM staff")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute('''
    SELECT staff.staff_name, divisions.division_name
    FROM staff
    LEFT JOIN divisions ON staff.division_id = divisions.division_id

    UNION

    SELECT staff.staff_name, divisions.division_name
    FROM divisions
    LEFT JOIN staff ON staff.division_id = divisions.division_id;
''')

print("\n Full Outer Join \n")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()
