#!/usr/bin/python3
"""_summary_
    Test suite for the User class in models.user
"""
import unittest
from models.base_model import BaseModel

from models.user import User


class TestUser(unittest.TestCase):
    """_summary_
        Test cases against the User class
    """

    def test_creation(self):
        '''this test validate that creation proccess was correct.
        '''

        data = {'id': 3,
                'fist_name': 'Ronald',
                'last_name': 'Abimbola',
                'password': '@b1mb0l@_RD',
                'email': 'r.abimbola@alustudent.com',
                }

        self.user = User(**data)
        self.assertEqual(self.user.id, 3)
        self.assertEqual(self.user.first_name, 'Ronald')
        self.assertEqual(self.user.first_name, 'Abimbola')
        self.assertEqual(self.user.password, '@b1mb0l@_RD')
        self.assertEqual(self.user.email, 'r.abimbola@alustudent.com')

    def test_attrs_are_class_attrs(self):
        user = User()
        self.assertTrue(hasattr(User, "first_name") and hasattr(User, "last_name"))

    def test_class_attrs(self):
        user = User()
        self.assertIs(type(user.first_name), str)
        self.assertIs(type(user.last_name), str)
        self.assertTrue(user.first_name == "")
        self.assertTrue(user.last_name == "")

    def test_user_is_a_subclass_of_basemodel(self):
        user = User()
        self.assertTrue(issubclass(type(user), BaseModel))


if __name__ == "__main__":
    unittest.main()
