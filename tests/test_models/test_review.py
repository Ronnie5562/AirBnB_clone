#!/usr/bin/python3
"""_summary_
    Test suite for the Review class in models.review
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """_summary_
        This class test user class.
    """

    def setUp(self):
        self.review = Review()

    def test_creation(self):
        """ 
            This test validate that creation proccess was correct.
        """
        self.assertEqual(self.review.text, '')


if __name__ == "__main__":
    unittest.main()
