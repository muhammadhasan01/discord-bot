import unittest

from src.db import connect_db, create_table_todos, insert_todo_task, show_todo_task, update_task_status


class MyTestCase(unittest.TestCase):
    db = None

    @classmethod
    def setUpClass(cls):
        cls.db = connect_db()

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

    def test_connect_db(self):
        self.assertTrue(self.db.is_connected())

    def test_create_table_todos(self):
        create_table_todos(self.db)
        cursor = self.db.cursor()
        cursor.execute("SHOW TABLES LIKE 'todos'")
        self.assertGreaterEqual(len(cursor.fetchall()), 1)

    def test_insert_todo_task(self):
        row_id = insert_todo_task(self.db, "task")
        self.assertIsInstance(row_id, int)
        self.assertGreaterEqual(row_id, 1)

    def test_show_todo_task(self):
        result = show_todo_task(self.db)
        self.assertIsInstance(result, list)

    def test_update_task_status(self):
        row_id = insert_todo_task(self.db, "task")
        cnt = update_task_status(self.db, row_id, 1)
        self.assertEqual(cnt, 1)


if __name__ == '__main__':
    unittest.main()
