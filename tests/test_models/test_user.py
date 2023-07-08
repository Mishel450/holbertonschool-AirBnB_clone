#!/usr/bin/python3
""""""
import unittest
from models.user import User
from datetime import datetime

class Test_User(unittest.TestCase):
    """"""

    def test_create_cbject(self):
        Us = User()
        self.assertIsInstance(Us, User)

    def test_check_id(self):
        Us = User()
        self.assertIsInstance(Us.id, str)

    def test_check_created_at(self):
        Us = User()
        self.assertIsInstance(Us.created_at, datetime)

    def test_check_updated_at(self):
        Us = User()
        self.assertIsInstance(Us.updated_at, datetime)

    def test_save(self):
        Us = User()
        hs = Us.updated_at
        Us.save()
        new_hs = Us.updated_at
        self.assertNotEqual(hs, new_hs)  # verifica si el hs no es iguales a new_hs

    def test_to_dict(self):
        Us = User()
        dict_result = Us.to_dict()
        self.assertIsInstance(dict_result, dict)
        self.assertIn("__class__", dict_result)
        self.assertEqual(dict_result["__class__"], "User")
        self.assertIn("updated_at", dict_result)

    def test_check_email(self):
        Us = User()
        self.assertEqual(Us.email, '')

    def test_check_password(self):
        Us = User()
        self.assertEqual(Us.password, '')

    def test_check_first_name(self):
        Us = User()
        self.assertEqual(Us.first_name, '')

    def test_check_last_name(self):
        Us = User()
        self.assertEqual(Us.last_name, '')