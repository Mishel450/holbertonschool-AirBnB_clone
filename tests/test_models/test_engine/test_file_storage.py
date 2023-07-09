#!/usr/bin/python3
"""test of file_storage"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import json


class FileStorageTest(unittest.TestCase):
    """test"""

    def setUp(self):
        self.fs = FileStorage()

    def tearDown(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_file_path(self):
        expected_path = "file.json"
        self.assertEqual(self.fs._FileStorage__file_path, expected_path)

    def test_all(self):
        self.assertIsInstance(self.fs.all(), dict)

    def test_all_2(self):
        fs = FileStorage()
        obj = fs.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, fs._FileStorage__objects)

    def test_all_object(self):
        fs = FileStorage()
        object = fs.all()
        self.assertEqual(fs.all(), object)

    def test_new(self):
        bm = BaseModel()
        self.fs.new(bm)
        key = "{}.{}".format(type(bm).__name__, bm.id)
        self.assertEqual(bm, self.fs.all()[key])

    def test_save(self):
        bm = BaseModel()
        self.fs.new(bm)
        self.fs.save()
        with open(FileStorage._FileStorage__file_path, "r") as file:
            file_content = file.read()
        self.assertIn(type(bm).__name__, file_content)
        self.assertIn(bm.id, file_content)

    def test_reload(self):
        bm = BaseModel()
        self.fs.new(bm)
        key = 'BaseModel.' + bm.id
        self.fs.save()
        self.fs.reload()
        self.assertEqual(bm.to_dict(), self.fs.all()[key].to_dict())

    def test_everything(self):
        fs = FileStorage()
        fs.all().clear()
        fs.reload()
        self.assertTrue(len(fs.all()) > 0)
