#!/usr/bin/python3
""""""
import unittest
from models.city import City
from datetime import datetime


class Test_city(unittest.TestCase):
    """"""

    def test_check_state_id(self):
       ct = City()
       self.assertEqual(ct.state_id, '')

    def test_check_name(self):
        ct = City()
        self.assertEqual(ct.name, '')
