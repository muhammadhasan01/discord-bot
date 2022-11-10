import os
import unittest

from dotenv import load_dotenv

from src.db import connect_db, create_table_todos, clear_todo_tasks
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
        self.assertEqual(f"Task of \"task 1\" was successfully added with an `id={res[0]}`", msg)

    def test_view_task_success_empty(self):
        clear_todo_tasks(self.db)
        msg = todo_handler(self.db, '$todo view')
        self.assertEqual("Your todo list is empty...", msg)

    def test_update_task_invalid(self):
        msg = todo_handler(self.db, '$todo update 3923 arg')
        self.assertEqual("Invalid query, format update should be: \"$query format {id}\"", msg)


if __name__ == '__main__':
    unittest.main()
