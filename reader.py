import sqlite3

def show_items(DB_NAME):
    db = sqlite3.connect(DB_NAME)
    try:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM items")
        all_items = cursor.fetchall()
        print("Список предметов:")
        if not all_items:
            print("Предметов нет")
        else:
            for item in all_items:
                print(f"ID:{item[0]}, Название: {item[1]}, Описание: {item[2]}, редкость: {item[3]}")
    finally:
        db.close()