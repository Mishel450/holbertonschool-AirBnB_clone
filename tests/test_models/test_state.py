#!/usr/bin/python3
"""state"""
import unittest
from models.state import State


class Test_State(unittest.TestCase):
    """This class contains test methods to test the
    behavior of the State class."""

    def test_check_name(self):
        St = State()
        self.assertEqual(St.name, '')
