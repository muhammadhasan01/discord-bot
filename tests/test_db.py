import unittest

from src.db import connect_db


class MyTestCase(unittest.TestCase):
    def test_connect_db(self):
        mydb = connect_db()
        self.assertTrue(mydb.is_connected())
        mydb.close()


if __name__ == '__main__':
    unittest.main()
