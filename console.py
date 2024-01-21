#!/usr/bin/python3

"""
This contains the entry point of the command interpreter
"""

import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    
    """This will contain specific behavior of the command line interface"""

    prompt = "(hbnb)"

    def emptyline(self):
        """Return an empty line"""
        pass

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def help_quit(self, arg):
        """Show information about the quit command"""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """Exit the program on EOF"""
        print()
        return True

    def do_create(self, arg):
        """Create a new instance for BaseModel"""
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("Class name missing")
        else:
            class_name = commands[0]
            valid_classes = [BaseModel, User]  # Add more classes as needed
            if any(isinstance(valid_class, type) for valid_class in valid_classes):
                new_instance = valid_classes[class_name]()
                storage.save()
                print(new_instance.id)
            else:
                print("Invalid class name")

    def do_show(self, arg):
        """Show string representation of an instance"""
        # ...

    def do_destroy(self, arg):
        """Delete an instance"""
        # ...

    def do_all(self, arg):
        """Print the string of all instances or a specific class"""
        objects = storage.all()
        commands = shlex.split(arg)

        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        else:
            class_name = commands[0]
            valid_classes = [BaseModel, User]  # Add more classes as needed
            if any(isinstance(valid_class, type) for valid_class in valid_classes):
                for key, value in objects.items():
                    if isinstance(value, valid_classes[class_name]):
                        print(str(value))
            else:
                print("Invalid class name")

    def do_update(self, arg):
        """Update an instance"""
        # ...


if __name__ == "__main__":
    HBNBCommand().cmdloop()

