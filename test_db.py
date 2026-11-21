import os
import tempfile
import unittest

import DBdriver


class TestDB(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_name = os.path.join(self.temp_dir.name, "test_items.db")
        DBdriver.init_db(self.db_name)

    def tearDown(self):
        self.temp_dir.cleanup()


    def _seed_one_item(self):
        """Insert a single item and return its id."""
        DBdriver.insert_items(
            self.db_name,
            "Меч",
            "Обычный железный меч",
            2,
        )
        items = DBdriver.get_list(self.db_name)
        self.assertEqual(len(items), 1, "seed failed: expected exactly one row")
        return items[0][0]


    def test_new_db_is_empty(self):
        self.assertEqual(DBdriver.get_list(self.db_name), [])


    def test_added_item_is_in_list(self):
        self._seed_one_item()

        items = DBdriver.get_list(self.db_name)

        self.assertEqual(len(items), 1)
        item_id, name, description, rarity = items[0]
        self.assertIsNotNone(item_id)
        self.assertEqual(name, "Меч")
        self.assertEqual(description, "Обычный железный меч")
        self.assertEqual(rarity, 2)

    def test_multiple_items_preserve_insert_order(self):
        DBdriver.insert_items(self.db_name, "Меч", "Железный", 2)
        DBdriver.insert_items(self.db_name, "Щит", "Деревянный", 1)
        DBdriver.insert_items(self.db_name, "Лук", "Охотничий", 3)

        names = [row[1] for row in DBdriver.get_list(self.db_name)]
        self.assertEqual(names, ["Меч", "Щит", "Лук"])


    def test_find_existing_item(self):
        item_id = self._seed_one_item()

        item = DBdriver.find_item(item_id, self.db_name)

        self.assertIsNotNone(item)
        self.assertEqual(item[0], item_id)
        self.assertEqual(item[1], "Меч")
        self.assertEqual(item[2], "Обычный железный меч")
        self.assertEqual(item[3], 2)

    def test_find_missing_item_returns_none(self):
        self._seed_one_item()
        self.assertIsNone(DBdriver.find_item(999, self.db_name))

    def test_find_on_empty_db_returns_none(self):
        self.assertIsNone(DBdriver.find_item(1, self.db_name))


    def test_change_item_updates_fields(self):
        item_id = self._seed_one_item()

        DBdriver.change_item(
            item_id, self.db_name,
            "Острый меч", "Острый стальной меч", 3,
        )

        item = DBdriver.find_item(item_id, self.db_name)
        self.assertEqual(item[1], "Острый меч")
        self.assertEqual(item[2], "Острый стальной меч")
        self.assertEqual(item[3], 3)

    def test_change_item_does_not_affect_other_rows(self):
        DBdriver.insert_items(self.db_name, "Меч", "Железный", 2)
        DBdriver.insert_items(self.db_name, "Щит", "Деревянный", 1)

        DBdriver.change_item(1, self.db_name, "Меч+", "Лучше", 4)

        first = DBdriver.find_item(1, self.db_name)
        second = DBdriver.find_item(2, self.db_name)
        self.assertEqual(first[1:], ("Меч+", "Лучше", 4))
        self.assertEqual(second[1:], ("Щит", "Деревянный", 1))

    def test_change_nonexistent_item_is_noop(self):
        """A change targeting an unknown id must not create a row or raise."""
        DBdriver.change_item(999, self.db_name, "X", "Y", 1)
        self.assertEqual(DBdriver.get_list(self.db_name), [])

    def test_change_with_boundary_rarities(self):
        item_id = self._seed_one_item()

        for rarity in (1, 6):
            with self.subTest(rarity=rarity):
                DBdriver.change_item(item_id, self.db_name, "Меч", "Описание", rarity)
                self.assertEqual(
                    DBdriver.find_item(item_id, self.db_name)[3], rarity
                )

if __name__ == "__main__":
    unittest.main()