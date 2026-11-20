import sqlite3,inputer,reader
from contextlib import closing

DB_NAME = 'items.db'

SCHEMA = """
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item TEXT NOT NULL,
        description TEXT NOT NULL,
        rarity int NOT NULL DEFAULT 1
    )
"""

def init_db(db):
    db.execute(SCHEMA)

def main():
    with closing(sqlite3.connect(DB_NAME)) as db:
        with db:
            init_db(db)
    while True:
        print("Нажмите соответствующую цифру чтобы выйти")
        print("добавить новый предмет(1)")
        print("посмотреть список предметов(2)")
        print("выйти(0)")
        target = input("Что вы хотите сделать?").strip()
        match target:
            case "1":
                inputer.input_item(DB_NAME)
            case "2":
                reader.show_items(DB_NAME)
            case "0":
                print("спасибо за внимание")
                return
            case _:
                print("выберите один из вариантов")

if __name__ == "__main__":
    main()