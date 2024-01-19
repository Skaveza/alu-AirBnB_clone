#!/usr/bin/python3
"""
this contains entry point of the command interpreter
"""
import cmd
import shlex
from models.base model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    this will contain specific behaiviour of the command line interface
    """
    prompt = "(hbnb)"
    valid_classes = ["BaseModel"]

    def emptyline(self):
        """
     return an empty line
        """

        pass

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

    def do_create(self, arg):
        """
        create a new instance for BaseModel
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("class name missing")
        elif commands[0] not in self.valid_classes:
            print("class does not exist")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)



    def do_show(self, arg):
        """
        show string represantation of an instance
        """

        commands = shlex.split(arg)

        if len(commands) == 0:
            print("class name missing")
        elif commands[0] not in self.valid_classes:
            print("class does not exist")
        elif len(commands) < 2:
            print("instance id missing")
        else:
            objects = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("no instance")



    def do_destroy(self, arg):
        """
        delete an instance
        """

        commands = shlex.split(arg)

        if len(commands) == 0:
            print("class name missing")
        elif commands[0] not in self.valid_classes:
            print("class does not exist")
        elif len(commands) < 2:
            print("instance id missing")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("no instance found")

    def do_all(self, arg):
        """
        print the string of all inbstance or a specific class"
        """

        objects = storage.all()

        commands = shlex.split(arg)

        if len(commands) == 0:
            for key, value in objects.items()
                print(str(value))
        elif commands[0] not in self.valid_classes:
            print("class does not exist")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))


    def do_update(self, arg):
        """
        update an instance
        """

        commands = shlex.split(arg)

        if len(commands) == 0:
            print("class name missing")
        elif commands[0]not in self.valid_classes:
            print("class does not exist")
        elif len(commands) < 2:
            print("instance id missing")
        else:
            objects = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key not in objects:
                print("no instance found")
                elif len(commands) < 3:
                    print("attribute name missing")
                elif len(commands) < 4:
                    print("value missing")
                else:
                    obj = objects[key]

                    attr_name = commands[2]
                    attr_value = commands[3]

                    try:
                        attr_value = eval(attr_value)
                    except Exception
                        pass
                    setattr(obj, attr_name, attr_value)

                    obj.save()


                    

if __name__ == "__main__":
    HBNBCommand().cmdloop
