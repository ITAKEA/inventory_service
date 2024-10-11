import sqlite3
import os

db_path = os.getenv('DB_PATH')

def init_db():
    with sqlite3.connect('db.db') as conn:
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS inventory (
                        product_id INTEGER PRIMARY KEY,
                        stock INTEGER
                    )''')
        
        cur.execute('SELECT COUNT(*) FROM inventory')
        row_count = cur.fetchone()[0]

        if row_count == 0:
            cur.executemany('''INSERT INTO inventory (
                            "product_id", 
                            "stock") 
                            VALUES (:product_id,:stock)''', db_list)


def read(id):
    with sqlite3.connect('db.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM inventory WHERE product_id = ?', (id,))
        product = cur.fetchone()

    return product

def create(inventory):
    with sqlite3.connect('db.db') as conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO inventory (product_id, stock) VALUES (?,?)', inventory )


def update(inventory):
    with sqlite3.connect('db.db') as conn:
        cur = conn.cursor()
        prod = read(inventory[0])
        cur.execute('UPDATE inventory SET stock = ? WHERE product_id = ?', (inventory[1]+prod[1], inventory[0]) )

"""
db = {
    121: {"product_id": 121, "stock": 100},
    122: {"product_id": 122, "stock": 50},
    123: {"product_id": 123, "stock": 75}
    # Add more products as needed
}
"""

db_list =[
    {"product_id": 121, "stock": 100},
    {"product_id": 122, "stock": 50},
    {"product_id": 123, "stock": 75},
    {"product_id": 124, "stock": 0},
    {"product_id": 125, "stock": 10},
    {"product_id": 126, "stock": 110},
    {"product_id": 127, "stock": 0},
    {"product_id": 128, "stock": 1},
    {"product_id": 129, "stock": 11},
    {"product_id": 130, "stock": 14},
    {"product_id": 131, "stock": 18},
    {"product_id": 132, "stock": 19},
    {"product_id": 133, "stock": 19},
    {"product_id": 134, "stock": 5},
    {"product_id": 135, "stock": 4},
    {"product_id": 136, "stock": 3}
    ]