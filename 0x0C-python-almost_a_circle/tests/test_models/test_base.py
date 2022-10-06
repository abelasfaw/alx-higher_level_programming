#!/usr/bin/python3
"""test suite for Base class"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for class Base"""

    def test_auto_id(self):
        """checks if id is auto generated"""
        self.assertEqual(1, Base().id)

    def test_id_increment(self):
        """checkis if id is incremented from previous value"""
        prev = Base().id
        self.assertEqual((prev + 1), Base().id)
