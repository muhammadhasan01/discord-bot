import unittest

from src.db import connect_db, create_table_todos


class MyTestCase(unittest.TestCase):
    def test_connect_db(self):
        mydb = connect_db()
        self.assertTrue(mydb.is_connected())
        mydb.close()

    def test_create_table_todos(self):
        mydb = connect_db()
        create_table_todos(mydb)
        cursor = mydb.cursor()
        cursor.execute("SHOW TABLES LIKE 'todos'")
        self.assertGreaterEqual(len(cursor.fetchall()), 1)


if __name__ == '__main__':
    unittest.main()
