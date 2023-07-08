#!/usr/bin/python3
""""""
import unittest
from models.review import Review



class TestReview(unittest.TestCase):
    """"""

    def test_check_place_id(self):
        Re = Review()
        self.assertEqual(Re.place_id, '')

    def test_check_user_id(self):
        Re = Review()
        self.assertEqual(Re.user_id, '')

    def test_check_text(self):
        Re = Review()
        self.assertEqual(Re.text, '')
