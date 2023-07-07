#!/usr/bin/python3
""""""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def test_create_object(self):
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)

    def test_check_id(self):
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)

    def test_check_created_at(self):
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime)

    def test_check_updated_at(self):
        bm = BaseModel()
        self.assertIsInstance(bm.updated_at, datetime)

    def test_save(self):
        bm = BaseModel()
        hs = bm.updated_at
        bm.save()
        new_hs = bm.updated_at
        self.assertNotEqual(hs, new_hs)
