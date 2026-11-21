import sqlite3
from contextlib import closing

SCHEMA = """
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item TEXT NOT NULL,
        description TEXT NOT NULL,
        rarity int NOT NULL DEFAULT 1
    )
"""

def init_db(db_name):
    with closing(sqlite3.connect(db_name)) as db:
        with db:
            db.execute(SCHEMA)

def insert_items(db_name, item, description,rarity):
        with closing(sqlite3.connect(db_name)) as db:
            with db:
                add_item(db, item, description,rarity)

def add_item(db, item, description,rarity):
    db.execute(
        "INSERT INTO items (item, description,rarity) VALUES (?, ?,?)",
        (item, description,rarity),
    )


def get_list(db_name):
    with closing(sqlite3.connect(db_name)) as db:
        cursor = db.execute(
            "SELECT * FROM items ORDER BY id"
        )
        return cursor.fetchall()

def find_item(item_id,db_name):
    with closing(sqlite3.connect(db_name)) as db:
        cursor = db.execute(
            "SELECT * FROM items where id=?",(item_id,)
        )
        return cursor.fetchone()

def change_item(target_ID,db_name,new_name,new_description,new_rarity):
    with closing(sqlite3.connect(db_name)) as db:
        with db:
            db.execute(
                "UPDATE items set item=?, description=?, rarity=? where id=?",(new_name, new_description,new_rarity,target_ID)
            )
        return()