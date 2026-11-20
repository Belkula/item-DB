import sqlite3,inputer
from contextlib import closing

DB_NAME = 'items.db'

def main():
    inputer.input_item(DB_NAME)

if __name__ == "__main__":
    main()