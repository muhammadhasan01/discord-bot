import unittest

from src.quote import get_quote

SEPARATOR = '-'


def test_get_quote_have_separator():
    quote = get_quote()
    assert SEPARATOR in quote


def test_get_quote_have_content():
    data = get_quote().split(f' {SEPARATOR} ')
    assert len(data) >= 1
    assert isinstance(data[0], str)


def test_get_quote_have_author():
    data = get_quote().split(f' {SEPARATOR} ')
    assert len(data) >= 2
    assert isinstance(data[1], str)


if __name__ == '__main__':
    unittest.main()
