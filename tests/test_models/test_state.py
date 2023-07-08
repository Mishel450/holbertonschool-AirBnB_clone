#!/usr/bin/python3
""""""
import unittest
from models.state import State


class Test_State(unittest.TestCase):
    """"""

    def test_check_name(self):
        St = State()
        self.assertEqual(St.name, '')
