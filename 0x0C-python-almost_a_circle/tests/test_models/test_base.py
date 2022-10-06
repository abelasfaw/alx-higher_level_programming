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

    def test_id_save(self):
        """checks if generated id is saved"""
        self.assertEqual(Base().id, Base._nb_objects)

    def test_to_json_string_none(self):
        """validates output with None input"""
        self.assertEqual("[]", Base().to_json_string(None))

    def test_to_json_string_empty_list(self):
        """validates output with empty list input"""
        self.assertEqual("[]", Base().to_json_string([]))

    def test_to_json_string_valid(self):
        """validates output with expected input"""
        self.assertEqual('[{"id": 1}]', Base().to_json_string([{'id': 1}]))

    def test_to_json_string_valid_input_type(self):
        """validates type of output with expected input"""
        self.assertEqual(type("str"), type(Base().to_json_string([{'id': 1}])))
