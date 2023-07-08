#!/usr/bin/python3
""""""
import unittest
from models.user import User
from datetime import datetime

class Test_User(unittest.TestCase):
    """"""

    def Test_Create_Object(self):
        Us = User()
        self.assertIsInstance(Us, User)

    def Test_check_id(self):
        Us = User()
        self.assertIsInstance(Us.id, str)

    def Test_check_created_at(self):
        Us = User()
        self.assertIsInstance(Us.created_at, datetime)

    def Test_check_updated_at(self):
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

    def Test_check_email(self):
        Us = User()
        Us.email = "airBnB@gmail.com"
        self.assertIsInstance(Us.email, str)
        self.assertAlmostEqual(Us.email, "airBnB@gmail.com")

    def Test_check_password(self):
        Us = User()
        Us.password = "Gertrudis15"
        self.assertIsInstance(Us.password, str)
        self.assertAlmostEqual(Us.password, "Gertrudis15")

    def Test_check_first_name(self):
        Us = User()
        Us.first_name = "Gertrudis"
        self.assertIsInstance(Us.first_name, str)
        self.assertAlmostEqual(Us.first_name, "Gertrudis")

    def Test_check_last_name(self):
        Us = User()
        Us.last_name = "Gomez"
        self.assertIsInstance(Us.last_name, str)
        self.assertAlmostEqual(Us.last_name, "Gomez")