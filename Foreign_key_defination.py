import sqlite3

conn = sqlite3.connect('writer_book_relationship.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE writers (
        writer_id INTEGER PRIMARY KEY,
        writer_name TEXT NOT NULL);
''')

cursor.execute('''
    CREATE TABLE publications (
        publication_id INTEGER PRIMARY KEY,
        publication_title TEXT NOT NULL,
        writer_id INTEGER,
        FOREIGN KEY (writer_id) REFERENCES writers(writer_id));
''')

cursor.executemany('''
    INSERT INTO writers (writer_id, writer_name) 
    VALUES (?, ?);''', [
    (1, 'Agatha Christie'),
    (2, 'Isaac Asimov'),
    (3, 'Ray Bradbury')])

cursor.execute("SELECT * FROM writers")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.executemany('''
    INSERT INTO publications (publication_id, publication_title, writer_id) 
    VALUES (?, ?, ?);''', [
    (1, 'Murder on the Orient Express', 1),           
    (2, 'Foundation', 2),      
    (3, 'Fahrenheit 451', 3)])

cursor.execute("SELECT * FROM publications")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()
