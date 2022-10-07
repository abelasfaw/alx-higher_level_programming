#!/usr/bin/python3
"""Test suite for Sqaure class"""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_square_instance(self):
        s1 = Square(1)
        self.assertEqual(1, s1.size)

    def test_square_instance_size_x(self):
        s1 = Square(1, 2)
        self.assertEqual((1, 2), (s1.size, s1.x))

    def test_square_instance_size_x_y(self):
        s1 = Square(1, 2, 3)
        self.assertEqual((1, 2, 3), (s1.size, s1.x, s1.y))

    def test_square_invalid_size_type(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_square_invalid_x_type(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_square_invalid_y_type(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_square_all_args(self):
        s1 = Square(1, 2, 3, 4)
        self.assertEqual((1, 2, 3, 4), (s1.size, s1.x, s1.y, s1.id))

    def test_square_negative_size(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_square_negative_x(self):
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_square_negative_y(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_square_zero_size_value(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_square_str(self):
        s1 = Square(1, 1, 1, 1)
        self.assertEqual("[Square] (1) 1/1 - 1", s1.__str__())

    def test_square_to_dictionary(self):
        s1 = Square(1, 1, 1, 1)
        self.assertEqual({'id': 1, 'size': 1, 'x': 1, 'y': 1}, s1.to_dictionary())

    def test_square_upate(self):
        s1 = Square(1,1,1,1)
        s1.update()
        self.assertEqual(1, s1.id)

    def test_square_update_id(self):
        s1 = Square(1)
        s1.update(100)
        self.assertEqual(100, s1.id)
    
    def test_square_update_id_size(self):
        s1 = Square(1, 2)
        s1.update(11, 12)
        self.assertEqual((11, 12), (s1.id, s1.size))

    def test_square_update_id_size_x(self):
        s1 = Square(1, 2, 3)
        s1.update(11, 12, 13)
        self.assertEqual((11, 12, 13), (s1.id, s1.size, s1.x))
    
    def test_square_update_id_size_x_y(self):
        s1 = Square(1, 2, 3, 4)
        s1.update(5, 6, 7, 8)
        self.assertEqual((5, 6, 7, 8), (s1.id, s1.size, s1.x, s1.y))

    def test_square_update_id_2(self):
        s1 = Square(1)
        s1.update(**{'id': 100})
        self.assertEqual(100, s1.id)

    def test_square_update_id_size_2(self):
        s1 = Square(1)
        s1.update(**{'id': 100, 'size':10})
        self.assertEqual((100, 10), (s1.id, s1.size))

    def test_square_update_id_size_x_2(self):
        s1 = Square(1)
        s1.update(**{'id': 5, 'size': 6, 'x': 7})
        self.assertEqual((5, 6, 7), (s1.id, s1.size, s1.x))

    def test_square_update_id_size_x_y_2(self):
        s1 = Square(1)
        s1.update(**{'id': 5, 'size': 6, 'x': 7, 'y': 8})
        self.assertEqual((5, 6, 7, 8) , (s1.id, s1.size, s1.x, s1.y))

    def test_square_create_id(self):
        s1 = Square.create(**{'id': 90})
        self.assertEqual(90, s1.id)

    def test_square_create_id_size(self):
        s1 = Square.create(**{'id': 90, 'size': 91})
        self.assertEqual((90, 91), (s1.id, s1.size))

    def test_square_create_id_size_x(self):
        s1 = Square.create(**{'id': 90, 'size': 91, 'x': 92})
        self.assertEqual((90, 91, 92), (s1.id, s1.size, s1.x))

    def test_square_create_id_size_x_y(self):
        s1 = Square.create(**{'id':5, 'size':6, 'x':7, 'y':8})
        self.assertEqual((5, 6, 7, 8), (s1.id, s1.size, s1.x, s1.y))
