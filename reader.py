import DBdriver

def show_items(DB_NAME):
    all_items = DBdriver.get_list(DB_NAME)
    print("Список предметов:")
    if not all_items:
        print("Предметов нет")
    else:
        for item in all_items:
            print(f"ID:{item[0]}, Название: {item[1]}, Описание: {item[2]}, редкость: {item[3]}")