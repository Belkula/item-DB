import DBdriver

def edit_item(DB):
    target_ID=input("ID редактируемого предмета: ")
    try:
        target_ID = int(input("ID редактируемого предмета: "))
    except ValueError:
        print("ID должен быть целым числом")
        return
    item_data=DBdriver.find_item(target_ID,DB)
    if not item_data:
        print("Не удалось найти предмет")
        return()
    print("Предмет с ID:",target_ID)
    print(f"Название:{item_data[1]}; Описание: {item_data[2]}; Редкость:{item_data[3]}")
    print(f"Вы хотите заменить предмет {item_data[1]}?(y/n)")
    selection=input().strip().lower()
    match selection:
        case "y":
            change_item(target_ID,DB)
        case "n":
            return()

def change_item(target_ID,DB):
    print("Введите новые значения(если вы не хотите их менять, оставьте пустыми)")
    new_name=input("Новое название: ")
    new_description=input("Новое описание: ")
    new_rarity=input("Новая редкость: ")
    if new_rarity != "":
        try:
            rarity = int(new_rarity)
            if rarity < 1 or rarity > 6:
                print("редкость должна быть в диапазоне от 1 до 6. ...")
                new_rarity = ""
        except ValueError:
            print("редкость должна быть целым числом! ...")
            new_rarity = ""
    target_item_data=DBdriver.find_item(target_ID,DB)
    if new_name=="":
        new_name=target_item_data[1]
    if new_description=="":
        new_description=target_item_data[2]
    if new_rarity=="":
        new_rarity=target_item_data[3]
    print("Новые характеристики предмета. Подтвердить изменения?(y/n)")
    print(f"новое название:{new_name}; новое описание:{new_description}; новая редкость:{new_rarity}")
    select=input().strip().lower()
    match select:
        case "y":
            DBdriver.change_item(target_ID,DB,new_name,new_description,new_rarity)
            print("Данные изменены")
            return()
        case "n":
            print("Изменения отменены")
            return()

