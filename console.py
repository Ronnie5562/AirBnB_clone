#!/usr/bin/python3
"""_summary_
    ==> This module is the entry point of the command interpreter { console }.
Returns:
    _type_: _description_
"""
from shlex import split
import cmd
import re

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review


def parse(arg):
    curly_braces = re.search(r'\{(.*?)\}', arg)
    square_brackets = re.search(r'\[(.*?)\]', arg)

    if curly_braces is None:
        if square_brackets is None:
            #return [x.strip(",") for x in arg.split()]
            return [x.strip(",") for x in split(arg)]
        else:
            before_square_brackets = split(arg[0:square_brackets.span()[0]])
            args = [x.strip() for x in before_square_brackets]
            args.append()

class HBNBCommand(cmd.Cmd):
    """_summary_
    This is the main class that runs the console.

    Args:
        cmd (_type_): _description_
    """
    prompt = "(hbnb)"
    def do_EOF(self, argv):
        """_summary_
            Quits the program with a new line. - Ctrl + d
                ==> Any method that returns true quits the program.
        """
        print()
        return True
    
    def do_quit(self, exiargvt):
        """_summary_
            Quits the program with a new line.
                ==> Any method that returns true quits the program.
        """
        return True
    
    def emptyline(self):
        """_summary_
            This is executed when a User inputs an empty line + <ENTER> key
                ==> The program moves to the next line.
        """
        pass

    def do_create(self, argv):





if __name__ == '__main__':
    HBNBCommand().cmdloop()
