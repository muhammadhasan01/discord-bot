import unittest

from src.db import connect_db, create_table_todos, insert_todo_task, show_todo_task


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
        mydb.close()

    def test_insert_todo_task(self):
        mydb = connect_db()
        row_count = insert_todo_task(mydb, "task")
        self.assertEqual(row_count, 1)
        mydb.close()

    def test_show_todo_task(self):
        mydb = connect_db()
        result = show_todo_task(mydb)
        self.assertIsInstance(result, list)


if __name__ == '__main__':
    unittest.main()
