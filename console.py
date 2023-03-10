#!/usr/bin/python3
"""_summary_
    ==> This module is the entry point of the command interpreter { console }.
Returns:
    _type_: _description_
"""
from shlex import split
import cmd
import re
import os

import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review

CLASSES = [
    "BaseModel",
    "User",
    "City",
    "Place",
    "State",
    "Amenity",
    "Review"
]

def parse(arg):
    curly_braces = re.search(r'\{(.*?)\}', arg)
    square_brackets = re.search(r'\[(.*?)\]', arg)

    if curly_braces is None:
        if square_brackets is None:
            #return [x.strip(",") for x in arg.split()]
            return [x.strip(",") for x in split(arg)]
        else:
            before_square_brackets = split(arg[0:square_brackets.span()[0]])
            args = [x.strip(",") for x in before_square_brackets]
            args.append(square_brackets.group())
            return args
    else:
        before_curly_braces = split(arg[0:curly_braces.span()[0]])
        args = [x.strip(",") for x in before_curly_braces]
        args.append(curly_braces.group())
        return args


def validate_args(args):
    """checks if args is valid

    Args:
        args (str): the string containing the arguments passed to a command

    Returns:
        Error message if args is None or not a valid class, else the arguments
    """
    arg_list = parse(args)

    if len(arg_list) == 0:
        print("** class name missing **")
    elif arg_list[0] not in CLASSES:
        print("** class doesn't exist **")
    else:
        return arg_list


class HBNBCommand(cmd.Cmd):
    """_summary_
    This is the main class that runs the console.

    Args:
        cmd (_type_): _description_
    """
    prompt = "(hbnb)"
    storage = models.storage

    def emptyline(self):
        """_summary_
            This is executed when a User inputs an empty line + <ENTER> key
                ==> The program moves to the next line.
        """
        pass

    def default(self, arg):
        """Default behaviour for cmd module when input is invalid"""
        action_map = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update,
            "create": self.do_create
        }

        match = re.search(r"\.", arg)
        if match:
            arg1 = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg1[1])
            if match:
                command = [arg1[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in action_map:
                    call = "{} {}".format(arg1[0], command[1])
                    return action_map[command[0]](call)

        print("*** Unknown syntax: {}".format(arg))
        return False

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
    

    def do_create(self, argv):
        """_summary_
            It creates a new instance of BaseModel and saves it.

        Args:
            argv : argument
        Return:
            It prints out the id of the newly created instance
        """
        val_args = validate_args(argv)
        if val_args:
            print(eval(val_args[0])().id)
            self.storage.save()
        
    
    def do_show(self, argv):
        """_summary_
            Prints the string representation of an instance based on the class name and id. 
                ==> Usage: $ show BaseModel 1234-1234-1234.
        """
        args = parse(argv)
        if args:
            if len(args) != 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key in self.storage.all():
                    print(self.storage.all()[key])
                else:
                    print("** no instance found **")

    def do_all(self, argv):
        """_summary_
            Prints all string representation of all instances based or not on the class name. 
                ==> Usage: $ all BaseModel or $ all
            Args:
                argv: class_name
        """
        args = split(argv)
        objects = self.storage.all().values()
        if len(args) == 0:
            print(str(obj) for obj in objects)
        else:
            if args[0] not in CLASSES:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objects if args[0] in str(obj)])

    def do_destroy(self, argv):
        """_summary_
            Deletes an instance based on the class name and id (save the change into the JSON file). 
                ==> Usage: $ destroy BaseModel 1234-1234-1234

        Args:
            argv : class_name, id
        """
        arg_list = validate_args(argv)
        if arg_list:
            if len(arg_list) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(*arg_list)
                if key in self.storage.all():
                    del self.storage.all()[key]
                    self.storage.save()
                else:
                    print("** no instance found **")

    def do_clear(self, _):
        """
            Clears the terminal
                ==> Usage: clear
        """
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')


    def do_update(self, argv):
        """_summary_
            This command updates an instance based on its class and id
                ==> __syntax__
                    Usage: $ update <class name> <id> <attribute name> "<attribute value>"
                        __Example__:
                        update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        Args:
            argv : Update to be made
        """
        arg_list = validate_args(argv)
        if arg_list:
            if len(arg_list) == 1:
                print("** instance id missing **")
            else:
                instance_id = "{}.{}".format(arg_list[0], arg_list[1])
                if instance_id in self.storage.all():
                    if len(arg_list) == 2:
                        print("** attribute name missing **")
                    elif len(arg_list) == 3:
                        print("** value missing **")
                    else:
                        obj = self.storage.all()[instance_id]
                        if arg_list[2] in type(obj).__dict__:
                            v_type = type(obj.__class__.__dict__[arg_list[2]])
                            setattr(obj, arg_list[2], v_type(arg_list[3]))
                        else:
                            setattr(obj, arg_list[2], arg_list[3])
                else:
                    print("** no instance found **")
            self.storage.save()
        
    def do_count(self, arg):
        """_summary_
                Retrieves the number of instances of a specific class
                usage: 
        """
        model_class = parse(arg)
        count = 0
        for instance in models.storage.all().values():
            if model_class[0] == type(instance).__name__:
                count += 1
        print(count)




if __name__ == '__main__':
    HBNBCommand().cmdloop()
