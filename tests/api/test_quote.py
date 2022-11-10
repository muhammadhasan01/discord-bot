import unittest

from src.api.quote import get_quote

SEPARATOR = '-'


class TestQuote(unittest.TestCase):
    def test_get_quote_have_separator(self):
        quote = get_quote()
        self.assertIn(SEPARATOR, quote)

    def test_get_quote_have_content(self):
        data = get_quote().split(f' {SEPARATOR} ')
        self.assertGreaterEqual(len(data), 1)
        self.assertIsInstance(data[0], str)

    def test_get_quote_have_author(self):
        data = get_quote().split(f' {SEPARATOR} ')
        self.assertGreaterEqual(len(data), 2)
        self.assertIsInstance(data[1], str)


if __name__ == '__main__':
    unittest.main()
