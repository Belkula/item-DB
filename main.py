import inputer,reader,DBdriver

DB_NAME = 'items.db'

def main():
    DBdriver.init_db(DB_NAME)
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