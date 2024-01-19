#!/usr/bin/python3
"""
this contains entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    this will contain specific behaiviour of the command line interface
    """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """
        when quit is entered will exit the program
        """
        return True
    
    def help_quit(self, arg):
        """
        shows what will happened 
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
         """
        when EOF is entered will exit the program
        """
        print()
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop
