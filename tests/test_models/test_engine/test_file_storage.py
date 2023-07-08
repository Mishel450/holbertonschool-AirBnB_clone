#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import uuid
import json


class FileStorageTest(unittest.TestCase):
    def test_all(self):
        fs = FileStorage()
        objects = fs.all()
        self.assertEqual(objects, fs._FileStorage__objects)

    def test_new(self):
        fs = FileStorage()
        model_id = str(uuid.uuid4())
        u_at = "2017-06-14T22:31:03.285259"
        c_at = "2017-06-14T22:31:03.285255"
        bm = BaseModel(id=model_id, updated_at=u_at, created_at=c_at)
        fs.new(bm)
        key = f"{bm.__class__.__name__}.{bm.id}"
        obj_dict = fs.all()
        self.assertIn(key, obj_dict)
        self.assertEqual(obj_dict[key], bm)
        self.assertIsInstance(obj_dict[key], BaseModel)

    def test_save_reload(self):
        fs = FileStorage()
        obj1 = BaseModel()
        obj1.id = str(uuid.uuid4())
        fs.new(obj1)
        obj2 = BaseModel()
        obj2.id = str(uuid.uuid4())
        fs.new(obj2)
        fs.save()
        fs_reload = FileStorage()
        fs_reload.reload()
        reload_obj = fs_reload.all()
        self.assertIn('BaseModel.' + obj1.id, reload_obj)
        self.assertIn('BaseModel.' + obj2.id, reload_obj)
        self.assertEqual(reload_obj['BaseModel.' + obj1.id].to_dict(), obj1.to_dict())
        self.assertEqual(reload_obj['BaseModel.' + obj2.id].to_dict(), obj2.to_dict())
