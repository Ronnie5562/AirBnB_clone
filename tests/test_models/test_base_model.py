#!/usr/bin/env python3
"""
    Test suite for the BaseModel class present in models.base_model
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime, time
from time import sleep
import models

class TestBaseModel_initialization(unittest.TestCase):
    
    """ Unittests for the initialization of the BaseModel class """
    def test_no_initialization_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_models_unique_ids(self):
        mod1 = BaseModel()
        mod2 = BaseModel()
        self.assertNotEqual(mod1.id, mod2.id)

    def test_created_at(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_models_creation_time(self):
        mod1 = BaseModel()
        sleep(0.05)
        mod2 = BaseModel()
        self.assertLess(mod1.created_at, mod2.created_at)

    def test_models_update_time(self):
        mod1 = BaseModel()
        sleep(0.05)
        mod2 = BaseModel()
        self.assertLess(mod1.updated_at, mod2.updated_at)

    def test_args_and_kwargs(self):
        t = datetime.today()
        t_form = t.isoformat()
        mod = BaseModel("12", id="345", created_at=t_form, updated_at=t)
        self.assertEqual(mod.id, "345")
        self.assertEqual(mod.created_at, t)
        self.assertEqual(mod.updated_at, t)

    def test_None_kwargs(self):
        with self.assertRaises(TypeError):
                BaseModel(id=None, created_at=None, updated_at=None)

    def test_no_args(self):
        mod = BaseModel(None)
        self.assertNotIn(None, mod.__dict__.values())

class TestBaseModel_save(unittest.TestCase):                  
        """ Unittests for the save method """
        def test_save1(self):
                mod = BaseModel()
                sleep(0.05)
                updated_at1 = mod.updated_at
                mod.save()
                self.assertLess(updated_at1, mod.updated_at)

        def test_save2(self):
                mod = BaseModel()
                sleep(0.05)
                updated1 = mod.updated_at
                mod.save()
                update2 = mod.updated_at
                self.assertLess(updated1, update2)
                sleep(0.05)
                mod.save()
                self.assertLess(update2, mod.update_at)

class TestBaseModel_to_dict(unittest.TestCase):
        """ unittests for to_dict method """
        def test_dict_type(self):
                mod = BaseModel()
                self.assertTrue(dict, type(mod.to_dict()))

        def test_dict_keys(self):
                mod = BaseModel()
                mod_dict = mod.to_dict()
                self.assertIn('id', mod_dict)
                self.assertIn('created_at', mod_dict)
                self.assertIn('updated_at', mod_dict)
                self.assertIn('__class__', mod_dict)

        def test_dict_sample(self):
                t = datetime.today()
                mod = BaseModel()
                mod.id = '00'
                mod.created_at = mod.updated_at = t
                dict = {
                        'id': '00',
                        '__class__': 'BaseModel',
                        'created_at': t.isoformat(),
                        'updated_at': t.isoformat()
                        }
                self.assertDictEqual(mod.to_dict(), dict)


if __name__ == "__main__":
        unittest.main()
