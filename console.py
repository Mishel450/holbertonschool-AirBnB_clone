#!/usr/bin/python3
"""console"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Exit the program"""
        return True

    def do_EOF(self, args):
        """Exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel"""
        if not args:
            print("** class name missing **")
            return

        name = args
        clase = ["BaseModel"]

        if name not in clase:
            print("** class doesn't exist **")
            return

        if name == "BaseModel":
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """Prints the string of an instance based on the class name"""
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            key = arg[0] + '.' + arg[1]
            objects = storage.all()
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")
        
    def do_destroy(self, args):
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            key = arg[0] + '.' + arg[1]
            objects = storage.all()
            if key in objects:
                del objects[key]
            else:
                print("** no instance found **")

    def do_all(self, args):
        arg = args.split()
        if len(arg) > 0 and arg[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            objects = storage.all()
            print(objects)
        
if __name__ == "__main__":
    HBNBCommand().cmdloop()
