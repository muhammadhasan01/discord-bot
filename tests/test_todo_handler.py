import os
import unittest

from dotenv import load_dotenv

from src.db import connect_db, create_table_todos
from src.todo_handler import todo_handler


class TestTodoHandler(unittest.TestCase):
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

    def test_when_query_invalid(self):
        msg = todo_handler(self.db, "$todo")
        self.assertEqual("invalid query, $todo must have at least two argument", msg)

    def test_add_task_success(self):
        msg = todo_handler(self.db, '$todo add "task 1"')
        cursor = self.db.cursor()
        cursor.execute('SELECT id FROM todos ORDER BY id DESC LIMIT 1')
        res = cursor.fetchone()
        self.assertEqual(f'Task of "task 1" was successfully added with an id={res[0]}', msg)


if __name__ == '__main__':
    unittest.main()
