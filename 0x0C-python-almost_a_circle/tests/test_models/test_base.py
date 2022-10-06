#!/usr/bin/python3
"""test suite for Base class"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_auto_id(self):
        self.assertEqual(1, Base().id)
