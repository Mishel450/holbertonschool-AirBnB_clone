#!/usr/bin/python3
"""review"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """This class contains test methods to test the
    behavior of the Review class."""

    def test_check_place_id(self):
        Re = Review()
        self.assertEqual(Re.place_id, '')

    def test_check_user_id(self):
        Re = Review()
        self.assertEqual(Re.user_id, '')

    def test_check_text(self):
        Re = Review()
        self.assertEqual(Re.text, '')
