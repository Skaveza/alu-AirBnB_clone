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
        pass

    def default(self, line):
        print(f"Unknown command: {line}")

    def do_quit(self, arg):
        return True

    def help_quit(self, arg):
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("Class name missing")
        else:
            class_name = commands[0]
            valid_classes = [BaseModel, User]
            if any(isinstance(valid_class, type) for valid_class in valid_classes):
                new_instance = valid_classes[class_name]()
                storage.save()
                print(new_instance.id)
            else:
                print("Invalid class name")

    def do_show(self, arg):
        # ...

    def do_destroy(self, arg):
        # ...

    def do_all(self, arg):
        objects = storage.all()
        commands = shlex.split(arg)

        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        else:
            class_name = commands[0]
            valid_classes = [BaseModel, User]
            if any(isinstance(valid_class, type) for valid_class in valid_classes):
                for key, value in objects.items():
                    if isinstance(value, valid_classes[class_name]):
                        print(str(value))
            else:
                print("Invalid class name")

    def do_update(self, arg):
        # ...


if __name__ == "__main__":
    HBNBCommand().cmdloop()


