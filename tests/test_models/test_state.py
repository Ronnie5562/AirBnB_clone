#!/usr/bin/env python3
"""_summary_
    This module tests state module present in models.
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """_summary_
        This test_class tests the state module.
    """

    def setUp(self):
        self.state = State()

    def test_creation(self):
        """_summary_
            This test validate that creation of name.
        """
        self.assertEqual(self.state.name, '')


if __name__ == "__main__":
    unittest.main()
