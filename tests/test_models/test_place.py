#!/usr/bin/python3
""""""
import unittest
from models.place import Place


class Testplace(unittest.TestCase):
    """"""

    def test_check_city_id(self):
        Pl = Place()
        self.assertEqual(Pl.city_id, '')

    def test_check_user_id(self):
        Pl = Place()
        self.assertEqual(Pl.user_id, '')

    def test_check_name(self):
        Pl = Place()
        self.assertEqual(Pl.name, '')

    def test_check_description(self):
        Pl = Place()
        self.assertEqual(Pl.description, '')

    def test_check_number_rooms(self):
        Pl = Place()
        self.assertEqual(Pl.number_rooms, 0)

    def test_check_number_bathrooms(self):
        Pl = Place()
        self.assertEqual(Pl.number_bathrooms, 0)

    def test_check_max_guest(self):
        Pl = Place()
        self.assertEqual(Pl.max_guest, 0)

    def test_check_price_by_night(self):
        Pl = Place()
        self.assertEqual(Pl.price_by_night, 0)

    def test_check_latitude(self):
        Pl = Place()
        self.assertEqual(Pl.latitude, 0.0)

    def test_check_longitude(self):
        Pl = Place()
        self.assertEqual(Pl.longitude, 0.0)

    def test_check_amenity_ids(self):
        Pl = Place()
        self.assertEqual(Pl.amenity_ids, [])