#!/usr/bin/python3
"""Test suite for Rectangle class"""


import unittest
from unittest.mock import patch
from models.rectangle import Rectangle
from io import StringIO


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

    def test_rectangle_area(self):
        """validate area of rectangle"""
        self.assertEqual(2, Rectangle(1, 2).area())

    def test_rectagnle_string_format(self):
        """validate string format of instance"""
        self.assertEqual("[Rectangle] (5) 0/0 - 2/4", Rectangle(2, 4, 0, 0, 5).__str__())

    def test_rectangle_display_with_no_padding(self):
        with patch('sys.stdout', new=StringIO()) as test_out:
            Rectangle(1, 1).display()
            self.assertEqual("#\n", test_out.getvalue())

    def test_rectangle_display_without_y(self):
        with patch('sys.stdout', new=StringIO()) as test_out:
            Rectangle(2, 1, 1).display()
            self.assertEqual(" ##\n", test_out.getvalue())

    def test_rectangle_display(self):
        with patch('sys.stdout', new=StringIO()) as test_out:
            Rectangle(2, 1, 1, 1).display()
            self.assertEqual("\n ##\n", test_out.getvalue())

    def test_rectangle_to_dictionary(self):

        self.assertEqual({'id': 5, 'width': 2, 'height': 1, 'x': 1, 'y': 1},\
                Rectangle(2, 1, 1, 1, 5).to_dictionary())
    
    def test_rectangle_update(self):
        r1 = Rectangle(1, 1)
        r1.update(2, 2, 2)
        self.assertEqual((2, 2, 2), (r1.id, r1.width, r1.height))

    def test_rectangle_update_with_id(self):
        r1 = Rectangle(1, 1)
        r1.update(100)
        self.assertEqual(100, r1.id)

    def test_rectangle_update_id_and_width(self):
        r1 = Rectangle(1, 1)
        r1.update(100, 10)
        self.assertEqual((100, 10), (r1.id, r1.width))

    def test_rectangle_update_id_width_height(self):
        r1 = Rectangle(1, 1)
        r1.update(100, 10, 10)
        self.assertEqual((100, 10, 10), (r1.id, r1.width, r1.height))

    def test_rectangle_update_id_with_height_x(self):
        r1 = Rectangle(1, 1)
        r1.update(10, 10, 10, 10)
        self.assertEqual((10, 10, 10, 10), (r1.id, r1.width, r1.height, r1.x))

    def test_rectangle_update_id_width_height_x_y(self):
        r1 = Rectangle(1, 1)
        r1.update(2, 3, 4, 5, 6)
        self.assertEqual((2, 3, 4, 5, 6), (r1.id, r1.width, r1.height, r1.x, r1.y))

    def test_rectangle_update_id(self):
        r1 = Rectangle(1, 1)
        r1.update(**{'id': 89})
        self.assertEqual(89, r1.id)

    def test_rectangle_update_id_width_2(self):
        r1 = Rectangle(1, 1)
        r1.update(**{'id':89, 'width': 90})
        self.assertEqual((89, 90), (r1.id, r1.width))
    
    def test_rectangle_update_id_width_height_2(self):
        r1 = Rectangle(1, 1)
        r1.update(**{'id':89, 'width':90, 'height':91})
        self.assertEqual((89, 90, 91), (r1.id, r1.width, r1.height))

    def test_rectangle_update_id_width_height_x_2(self):
        r1 = Rectangle(1, 1)
        r1.update(**{'id':4, 'width':5, 'height':6, 'x':7})
        self.assertEqual((4, 5, 6, 7), (r1.id, r1.width, r1.height, r1.x))

    def test_rectangle_update_id_width_height_x_y_2(self):
        r1 = Rectangle(1, 1)
        r1.update(**{'id':2, 'width':3, 'height':4, 'x':5, 'y':6})
        self.assertEqual((2, 3, 4, 5, 6), (r1.id, r1.width, r1.height\
                , r1.x, r1.y))

    def test_create_id(self):
        r1 = Rectangle.create(**{'id': 90})
        self.assertEqual(90, r1.id)

    def test_create_id_width_height(self):
        r1 = Rectangle.create(**{'id':90, 'width':91, 'height':92})
        self.assertEqual((90, 91, 92), (r1.id, r1.width, r1.height))

    def test_create_id_width_height_x(self):
        r1 =  Rectangle.create(**{'id':10, 'width':11, 'height':12, 'x':13,\
                'y':14})
        self.assertEqual((10, 11, 12, 13), (r1.id, r1.width, r1.height, r1.x))

    def test_create_id_width_height_x_y(self):
        r1 = Rectangle.create(**{'id':1, 'width':2, 'height':3, 'x':4, 'y':5})
        self.assertEqual((1, 2, 3, 4, 5), (r1.id, r1.width, r1.height, r1.x,\
                r1.y))

