import unittest
from is_duplicate_file import is_duplicate


class TestDuplicateFunction(unittest.TestCase):
    def test_if_dictionary(self):
        data = {1: 'a', 2: 'b', 23: 'c'}
        is_duplicate(data, 3, 12)
        self.assertEqual(type(data), dict)


if __name__ == '__main__':
    unittest.main()
