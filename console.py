#!/usr/bin/python3
"""console"""
import cmd
from models.base_model import BaseModel


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

    def show(self, args):
        """Prints the string of an instance based on the class name"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
