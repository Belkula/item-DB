import sqlite3
from contextlib import closing

DB_NAME = 'items.db'

SCHEMA = """
    CREATE TABLE IF NOT EXISTS incidents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item TEXT NOT NULL,
        description TEXT NOT NULL,
        rarity int NOT NULL DEFAULT 1
    )
"""

def init_db(db):
    db.execute(SCHEMA)

def add_incident(db, item, description,rarity):
    db.execute(
        "INSERT INTO incidents (item, description,rarity) VALUES (?, ?,?)",
        (item, description,rarity),
    )

def main():
    equipment = input("название предмета: ").strip()
    description = input("описание предмета: ").strip()
    rarity_raw = input("редкость(от 1 до 6): ").strip()

    try:
        rarity=int(rarity_raw)
    except ValueError:
        print ("редкость должна быть целым числом!")
        return
    if rarity<1 or rarity>6:
        print("редкость должна быть в диапазоне от 1 до 6")
        return

    if not equipment or not description:
        print("название и описание не должны быть пустыми")
        return

    with closing(sqlite3.connect(DB_NAME)) as db:
        with db:
            init_db(db)
            add_incident(db, equipment, description,rarity)

    print("запись добавлена")

if __name__ == "__main__":
    main()