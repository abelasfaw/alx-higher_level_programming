#!/usr/bin/python3
"""Test suite for Rectangle class"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class"""
    def test_rectangle_required_args(self):
        """validate instance with required args only"""
        r = Rectangle(1, 2)
        self.assertEqual((1, 2), (r.width, r.height))

    def test_rectangle_one_optional_arg(self):
        """validate instance with one optional arg"""
        r = Rectangle(1, 2, 3)
        self.assertEqual((1, 2, 3), (r.width, r.height, r.x))

    def test_rectangle_two_optional_args(self):
        """validate instance with two optional args"""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual((1, 2, 3, 4), (r.width, r.height, r.x, r.y))

    def test_rectangle_invalid_arg1_type(self):
        """check raised exception with invalid argument 1 type"""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_rectangle_invalid_arg2_type(self):
        """check raised exception with invalid argument 2 type"""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_rectangle_invalid_arg3_type(self):
        """check raised exception with invalid argument 3 type"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_rectangle_invalid_arg4_type(self):
        """check raised exception with invaluid argument 5 type"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_rectangle_all_arguments(self):
        """validates attributes when all arguments are provided"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual((1, 2, 3, 4, 5), (r.width, r.height, r.x, r.y, r.id))

    def test_rectangle_negative_width(self):
        """check raised exception with negative width value"""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_rectangle_negative_height(self):
        """check raised exception with negative height value"""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_rectangle_zero_width(self):
        """check raised exception with zero width"""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_rectangle_zero_height(self):
        """check raised exception with zero height"""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_rectangle_negative_x(self):
        """check raised exception with negative x value"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_rectangle_negative_y(self):
        """check raised exception with negative y value"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)
