#!/usr/bin/python3
""""""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """"""

    def test_check_name(self):
        Am = Amenity()
        self.assertEqual(Am.name, '')
