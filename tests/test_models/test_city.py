#!/usr/bin/env python3
"""
    This module test the City class.
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """_summary_
        This class test City class present in models.
    """

    def setUp(self):
        self.city = City()
        self.attr_list = ["state_id", "name"]

    def test_creation(self):
        '''_summary_
            This test validate that creation proccess was correct.
        '''
        self.assertEqual(self.city.name, '')
    
    def test_city_is_a_subclass_of_basemodel(self):
        '''_summary_
            This test validate that City is a subclass of basemodel
        '''
        self.assertTrue(issubclass(type(self.city), BaseModel))


if __name__ == "__main__":
    unittest.main()
