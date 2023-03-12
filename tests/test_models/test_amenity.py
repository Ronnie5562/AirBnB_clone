#!/usr/bin/python3
"""
    This module test the Amenity class.
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel



class TestAmenity(unittest.TestCase):
    """_summary_
        This test_class tests the Amenity module present in models.
    """

    def setUp(self):
        """_summary_
            This is the setUp method for the test in this module.
        """
        self.amenity = Amenity()

    def test_creation(self):
        """_summary_
            This test validates that creation proccess was correct.
        """
        self.assertEqual(self.amenity.name, '')
    
    def test_amenity_is_a_subclass_of_basemodel(self):
        """_summary_
            This test validates that amenity is a subclass of basemodel.
        """
        self.assertTrue(issubclass(type(self.amenity), BaseModel))

    def test_attr_is_a_class_attr(self):
        """_summary_
            This test validates that amenity has an attribute of name.
        """
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_class_attr(self):
        """_summary_
            This test validates that name is a string
        """
        self.assertIs(type(self.amenity.name), str)
        self.assertFalse(bool(getattr(self.amenity, "name")))


if __name__ == "__main__":
    unittest.main()
