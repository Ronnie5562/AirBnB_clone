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
            Command to executed when User inputs an empty line + <ENTER> key
                ==> The program moves to the next line.
        """
        pass




if __name__ == '__main__':
    HBNBCommand().cmdloop()
