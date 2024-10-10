import sqlite3

conn = sqlite3.connect('ItemProviders_RightJoin.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE items (
        item_id INTEGER PRIMARY KEY,
        item_name TEXT NOT NULL
    );
''')

cursor.execute('''
    CREATE TABLE providers (
        provider_id INTEGER PRIMARY KEY,
        provider_name TEXT NOT NULL
    );
''')

cursor.execute('''
    CREATE TABLE item_providers (
        item_id INTEGER,
        provider_id INTEGER,
        FOREIGN KEY (item_id) REFERENCES items(item_id),
        FOREIGN KEY (provider_id) REFERENCES providers(provider_id)
    );
''')

cursor.executemany('''
    INSERT INTO items (item_id, item_name) 
    VALUES (?, ?);
''', [
    (1, 'Phone'),
    (2, 'Headphones'),
    (3, 'Speaker'),
    (4, 'Charger'),
    (5, 'Monitor')
])

cursor.execute("SELECT * FROM items")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.executemany('''
    INSERT INTO providers (provider_id, provider_name) 
    VALUES (?, ?);
''', [
    (1, 'Techtronics'),
    (2, 'Global Supplies'),
    (3, 'ElectroMart')
])

cursor.execute("SELECT * FROM providers")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.executemany('''
    INSERT INTO item_providers (item_id, provider_id) 
    VALUES (?, ?);
''', [
    (1, 1),  
    (2, 1),  
    (3, 2),  
    (4, 3)  
])

cursor.execute("SELECT * FROM item_providers")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute('''
    SELECT items.item_name, providers.provider_name  
    FROM items
    LEFT JOIN item_providers ON items.item_id = item_providers.item_id
    LEFT JOIN providers ON item_providers.provider_id = providers.provider_id;
''')

rows = cursor.fetchall()
print("Right Join")
for row in rows:
    print(row)

conn.commit()
conn.close()
