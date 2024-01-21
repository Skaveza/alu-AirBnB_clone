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
from models.review import Reviewx


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
       """
        # If the class name is missing,
        # print ** class name missing ** (ex: $ create)
        if len(args) < 1:
            print("** class name missing **")
            return
        # If the class name doesn’t exist,
        # print ** class doesn't exist ** (ex: $ create MyModel)

        # convert the args to a list
        args = args.split()

        # the 1st element of the list is the class name
        class_name = args[0]
        if class_name not in self.__all_classes:
            print("** class doesn't exist **")
            return
        # print(self.__all_classes)
        # eval() interprets a string as a piece of python code
        new_object = eval(class_name + "()")
        new_object.save()
        print(new_object.id)
        storage.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
         arg_list = args.split()
        objdict = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        elif arg_list[0] not in self.__all_classes:
            print("** class doesn't exist **")
            return
        elif len(arg_list) == 1:
            print("** instance id missing **")
            return

        object_key = "{}.{}".format(arg_list[0], arg_list[1])

        if object_key not in objdict:
            print("** no instance found **")
            return
        else:
            print(objdict[object_key])


    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        arg_list = args.split()
        all_objects = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        class_name = arg_list[0]
        if class_name not in self.__all_classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        instance_id = arg_list[1]

        object_key = "{}.{}".format(class_name, instance_id)

        if object_key not in all_objects.keys():
            print("** no instance found **")
        else:
            del all_objects[object_key]
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representations of all instances
        based or not on the class name.
        """
        arg_list = args.split()
        all_objects = storage.all()
        object_list = []
        if len(arg_list) == 0:
            for obj in all_objects.values():
                object_list.append(obj.__str__())
            print(list(object_list))
            return

        if len(arg_list) > 0 and arg_list[0] not in self.__all_classes:
            print("** class doesn't exist **")
            return
        class_name = arg_list[0]
        object_list = []

        for obj in all_objects:
            if class_name == all_objects[obj].__class__.__name__:
                object_list.append(str(all_objects[obj]))
        print(object_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating an attribute.
        """
        arg_list = args.split()
        all_objects = storage.all()

        if len(arg_list) == 0:
            print("** class name missing **")
            return False
        class_name = arg_list[0]

        if class_name not in self.__all_classes:
            print("** class doesn't exist **")
            return False

        if len(arg_list) == 1:
            print("** instance id missing **")
            return False

        instance_id = arg_list[1]
        object_key = "{}.{}".format(class_name, instance_id)

        if object_key not in all_objects:
            print("** no instance found **")
            return False

        if len(arg_list) == 2:
            print("** attribute name missing **")
            return False
        attribute_name = arg_list[2]

        if len(arg_list) == 3:
            print("** value missing **")
            return False
        attribute_value = arg_list[3]

        if attribute_value.isdigit():
            if isinstance(attribute_value, float):
                attribute_value = float(attribute_value)
            elif isinstance(attribute_value, int):
                attribute_value = int(attribute_value)

        # update BaseModel 00c0c670-e5f3-4603-9aa1-3caca5ee0e75
        # email "aibnb@mail.com"

        obj = all_objects[object_key]
        # check if the attribute exist already
        if attribute_name in obj.to_dict():
            attribute_original_type = type(obj[attribute_name])
            attribute_value = attribute_original_type(attribute_value)

            if attribute_original_type in {str, int, float}:
                attribute_value = attribute_original_type(attribute_value)
                obj[attribute_name] = attribute_value
        # if it doesn’t exist we add it
        else:
            obj.__dict__.update({attribute_name: attribute_value})

        storage.save()


if __name__ == "__main__":
    """
    Main function
    """
    HBNBCommand().cmdloop()

        

