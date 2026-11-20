import DBdriver

def input_item(DB_NAME):
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
    DBdriver.insert_items(DB_NAME,equipment,description,rarity)

    print("запись добавлена")