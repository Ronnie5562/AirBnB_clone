import cmd
class HBNBCommand(cmd.Cmd):
    def do_EOF(self):
        """_summary_
            Quits the program with a new line. - Ctrl + d
                ==> Any method that returns true quits the program.
        """
        print()
        return True
    
    def do_quit(self):
        """_summary_
            Quits the program with a new line.
                ==> Any method that returns true quits the program.
        """
        return True
    
    def emptyline(self):
        """_summary_
            Command to executed when empty line + <ENTER> key
                ==> The pr
        """
        pass




if __name__ == '__main__':
    HBNBCommand().cmdloop()
