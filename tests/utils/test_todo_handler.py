import os
import unittest

from dotenv import load_dotenv

from src.db.db import connect_db, create_table_todos, clear_todo_tasks, insert_todo_task
from src.utils.todo_handler import todo_handler


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
        self.assertEqual(f"Task of \"task 1\" was successfully added with an `id = {res[0]}`", msg)

    def test_view_task_success_empty(self):
        clear_todo_tasks(self.db)
        msg = todo_handler(self.db, '$todo view')
        self.assertEqual("Your todo list is empty...", msg)

    def test_update_task_invalid_args(self):
        msg = todo_handler(self.db, '$todo update 3923 arg1 arg2')
        self.assertEqual("Invalid query, format update should be: `$query update {id} [done|undone]`", msg)

    def test_update_task_invalid_status(self):
        msg = todo_handler(self.db,  '$todo update 1 arg')
        self.assertEqual("invalid status `value = arg`, value can only be `done` and `undone`", msg)

    def test_update_task_success(self):
        row_id = insert_todo_task(self.db, "task")
        msg = todo_handler(self.db, f'$todo update {row_id} done')
        self.assertEqual(f'Task with `id = {row_id}` successfully updated to `status = done`', msg)

    def test_select_task_invalid_args(self):
        msg = todo_handler(self.db, '$todo select 3923 arg1 arg2')
        self.assertEqual("Invalid query, format select should be: `$query select {id}`", msg)

    def test_select_task_invalid_id(self):
        msg = todo_handler(self.db, '$todo select -1')
        self.assertEqual("Task with `id = -1` does not exist...", msg)

    def test_select_task_success(self):
        row_id = insert_todo_task(self.db, "task")
        msg = todo_handler(self.db, f'$todo select {row_id}')
        self.assertEqual(f'Task of "task" with an id = {row_id} has a status of `NOT DONE`', msg)

    def test_delete_task_invalid_args(self):
        msg = todo_handler(self.db, '$todo delete 3923 arg1 arg2')
        self.assertEqual("Invalid query, format delete should be: `$query delete {id}`", msg)

    def test_delete_task_invalid_id(self):
        msg = todo_handler(self.db, '$todo delete -1')
        self.assertEqual("Cannot delete task with `id = -1`, make sure the task exist", msg)

    def test_delete_task_success(self):
        row_id = insert_todo_task(self.db, "task")
        msg = todo_handler(self.db, f'$todo delete {row_id}')
        self.assertEqual(f'Task with `id = {row_id}` successfully deleted!', msg)

    def test_clear_task_invalid_args(self):
        msg = todo_handler(self.db, '$todo clear arg')
        self.assertEqual("Invalid query, format clear should only be: `$query clear`", msg)

    def test_clear_task_success(self):
        msg = todo_handler(self.db, '$todo clear')
        self.assertEqual("Todo tasks have been successfully cleared", msg)


if __name__ == '__main__':
    unittest.main()
