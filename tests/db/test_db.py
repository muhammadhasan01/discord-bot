import os
import unittest

from dotenv import load_dotenv

from src.db.db import connect_db, \
    create_table_todos, \
    insert_todo_task, \
    show_todo_tasks, \
    update_task_status, \
    select_task, \
    delete_task, \
    clear_todo_tasks


class TestDatabase(unittest.TestCase):
    db = None

    @classmethod
    def setUpClass(cls):
        load_dotenv()
        cls.db = connect_db(
            host=os.getenv("TEST_HOST"),
            user=os.getenv("TEST_USER"),
            password=os.getenv("TEST_PASSWORD"),
            port=os.getenv("TEST_PORT"),
            database=os.getenv("TEST_DATABASE")
        )
        create_table_todos(cls.db)

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

    def test_connect_db(self):
        self.assertTrue(self.db.is_connected())

    def test_create_table_todos(self):
        cursor = self.db.cursor()
        cursor.execute("SHOW TABLES LIKE 'todos'")
        self.assertGreaterEqual(len(cursor.fetchall()), 1)

    def test_insert_todo_task(self):
        row_id = insert_todo_task(self.db, "task")
        self.assertIsInstance(row_id, int)
        self.assertGreaterEqual(row_id, 1)

    def test_show_todo_tasks(self):
        result = show_todo_tasks(self.db)
        self.assertIsInstance(result, list)

    def test_update_task_status(self):
        row_id = insert_todo_task(self.db, "task")
        cnt = update_task_status(self.db, row_id, 1)
        self.assertEqual(1, cnt)

    def test_select_task(self):
        row_id = insert_todo_task(self.db, "task")
        res_id, content, is_done = select_task(self.db, row_id)
        self.assertEqual(row_id, res_id)
        self.assertEqual("task", content)
        self.assertEqual(0, is_done)

    def test_delete_task(self):
        row_id = insert_todo_task(self.db, "task")
        cnt = delete_task(self.db, row_id)
        self.assertEqual(1, cnt)

    def test_clear_todo_tasks(self):
        clear_todo_tasks(self.db)
        res = show_todo_tasks(self.db)
        self.assertEqual(0, len(res))


if __name__ == '__main__':
    unittest.main()
