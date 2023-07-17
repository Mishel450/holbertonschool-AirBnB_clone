#!/usr/bin/python3
"""City"""
import unittest
from models.city import City
from datetime import datetime


class Test_city(unittest.TestCase):
    """This class contains test methods to test the
    behavior of the City class."""

    def test_check_state_id(self):
        ct = City()
        self.assertEqual(ct.state_id, '')

    def test_check_name(self):
        ct = City()
        self.assertEqual(ct.name, '')
