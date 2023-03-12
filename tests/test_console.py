'''
    module documentation
'''
import unittest
from models.base_model import BaseModel
import os
import sys
from console import HBNBCommand
from io import StringIO


class TestHBNBCommand(unittest.TestCase):
    """_summary_
        This class test HBNBCommand class.
    """

    def setUp(self) -> None:
        return super().setUp()

    def out_test(self, func, arg, expect):
        """Axiliar function to test some commands of the console"""
        std_out = StringIO()
        sys.stdout = std_out
        func(arg)
        output = std_out.getvalue()
        self.assertEqual(output, expect + '\n')
        return output

    def test_creation_failed(self):
        """Testing the 'create' command of the console - the error messages"""
        try:
            os.remove('file.json')
        except:
            pass
        cmd = HBNBCommand()

        self.out_test(cmd.do_create, '', HBNBCommand.ERROR_CLASS_NAME)
        self.out_test(cmd.do_create, 'myModel', HBNBCommand.ERROR_CLASS)


    def test_create(self):
        cmd = HBNBCommand()
        #out = self.out_test(cmd.do_create, 'BaseModel', '')
    
    def test_do_all(self):
        cmd = HBNBCommand()
    def test_do_quit(self):
        cmd = HBNBCommand()
    def test_do_EOF(self):
        cmd = HBNBCommand()
    def test_do_show(self):
        cmd = HBNBCommand()
    def test_do_destroy(self):
        cmd = HBNBCommand()
    def test_do_update(self):
        cmd = HBNBCommand()
    
if __name__ == "__main__":
    unittest.main()
