import unittest

from src.todo_handler import todo_handler


class TestTodoHandler(unittest.TestCase):
    def test_when_query_invalid(self):
        res = todo_handler("$todo")
        self.assertEqual("invalid query, $todo must have at least two argument", res)


if __name__ == '__main__':
    unittest.main()
