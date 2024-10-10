import sqlite3

conn = sqlite3.connect('team_leads_selfjoin.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS team_members (
        member_id INTEGER PRIMARY KEY,
        member_name TEXT NOT NULL,
        leader_id INTEGER,
        FOREIGN KEY (leader_id) REFERENCES team_members(member_id)
    );
''')

cursor.executemany('''
    INSERT INTO team_members (member_id, member_name, leader_id) 
    VALUES (?, ?, ?);
''', [
    (1, 'Aditi', None),       
    (2, 'Rohan', 1),         
    (3, 'Sneha', 1),      
    (4, 'Vikram', 2),          
    (5, 'Meera', 2),      
    (6, 'Arjun', 3)         
])

cursor.execute("SELECT * FROM team_members")
rows = cursor.fetchall()
for row in rows:
    print(row) 

cursor.execute('''
    SELECT e.member_name AS Member, m.member_name AS Leader
    FROM team_members e
    LEFT JOIN team_members m ON e.leader_id = m.member_id;
''')

rows = cursor.fetchall()
print("\n Self Join \n")
for row in rows:
    print(row)

conn.commit()
conn.close()
