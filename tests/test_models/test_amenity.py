#!/usr/bin/python3
"""Amenty"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """This class contains the test methods to
    test the behavior of the Amenity class."""

    def test_check_name(self):
        """Checks if name of the Amenity class
    is initialized correctly as an empty string."""
        Am = Amenity()
        self.assertEqual(Am.name, '')
