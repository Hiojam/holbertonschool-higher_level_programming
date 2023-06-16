#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
"""Unittest for max_integer([])"""


class TestMaxNumber(unittest.TestCase):
    """ Test cases bases for max_integer function """

    def test_order_ascending(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_order_descending(self):
        result = max_integer([4, 3, 2, 1])
        self.assertEqual(result, 4)

    def test_order_unsorted(self):
        result = max_integer([2, 4, 1, 9, 5, 8])
        self.assertEqual(result, 9)

    def test_order_negatives(self):
        result = max_integer([-1, -3, -2, -9])
        self.assertEqual(result, -1)

    def test_order_nothing(self):
        result = max_integer([])
        self.assertEqual(result, None)

    def test_order_uniq(self):
        result = max_integer([8])
        self.assertEqual(result, 8)

    if __name__ == "__main__":
        unittest.main()
