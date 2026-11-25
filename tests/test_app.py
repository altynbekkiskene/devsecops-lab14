import unittest
from app import add_numbers


class TestAddition(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_rejects_string(self):
        with self.assertRaises(ValueError):
            add_numbers("2", 3)


if __name__ == "__main__":
    unittest.main()
