#!/usr/bin/python3
"""
This module defines the console for our project.
"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Defines the console.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF to exit the program.
        """
        return True

    def emptyline(self):
        """
        Ignore an empty line.
        """
        pass

    def do_create(self, arg):
        """
            Creates a new instance of a class,
            saves it (to the JSON file) and prints the id.
            Usage: create <class_name>
        $ create ModelName
        Throws an Error if ModelName is missing or doesnt exist"""
        args, n = parse(args)

        if not n:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif n == 1:
            # temp = classes[args[0]]()
            temp = eval(args[0])()
            print(temp.id)
            temp.save()
        else:
            print("** Too many argument for create **")
            pass

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.
        $ show MyModel instance_id
        Print error message if either MyModel or instance_id is missing
        Print an Error message for wrong MyModel or instance_id"""
        args, n = parse(arg)

        if not n:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")
        elif n == 2:
            try:
                inst = storage.find_by_id(*args)
                print(inst)
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")
        else:
            print("** Too many argument for show **")
            pass


    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        args, n = parse(arg)

        if not n:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")
        elif n == 2:
            try:
                storage.delete_by_id(*args)
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")
        else:
            print("** Too many argument for destroy **")
            pass


    def do_all(self, arg):
        """
        Prints all string representations of all instances
        based or not on the class name.
        """
        args, n = parse(args)

        if n < 2:
            try:
                print(storage.find_all(*args))
            except ModelNotFoundError:
                print("** class doesn't exist **")
        else:
            print("** Too many argument for all **")
            pass

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating an attribute.
        $ update Model id field value
        Throws errors for missing arguments"""
        args, n = parse(arg)
        if not n:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")
        elif n == 2:
            print("** attribute name missing **")
        elif n == 3:
            print("** value missing **")
        else:
            try:
                storage.update_one(*args[0:4])
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")


if __name__ == "__main__":
    """
    Main function
    """
    HBNBCommand().cmdloop()

        

