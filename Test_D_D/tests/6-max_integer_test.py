#!/usr/bin/env python
""" Unit test for max integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_neg_int(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def mixed_no(self):
        self.assertEqual(max_integer([-10, 0, 10, 5]), 10)

    def test_emptylist(self):
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([-10, 4, 6, 10]), 10)


if __name__ == '__main__':
    unittest.main()
