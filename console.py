#!/usr/bin/python3
"""
console.py module
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models


dic_obj = models.storage.all()


class HBNBCommand(cmd.Cmd):
    """HBNB console class"""

    prompt = '(hbnb) '
    __classes = {
            'BaseModel',
            'User',
            'State',
            'City',
            'Amenity',
            'Place',
            'Review'
            }

    def do_quit(self, arg):
        """Use "quit" command to exit"""
        return True

    def do_EOF(self, arg):
        """Press "ctrl + D" to EOF"""
        print()
        return True

    def emptyline(self):
        """Empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel and save in JSON"""
        arg_split = arg.split()
        if len(arg_split) == 0:
            print('** class name missing **')
        elif arg_split[0] in HBNBCommand.__classes:
            new_instance = eval(arg_split[0])()
            models.storage.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string base on a class name and id"""
        arg_split = arg.split()
        if len(arg_split) == 0:
            print('** class name missing **')
        elif arg_split[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_split) == 1:
            print('** instance id missing **')
        elif "{}.{}".format(arg_split[0], arg_split[1]) in dic_obj.keys():
            print(dic_obj["{}.{}".format(arg_split[0], arg_split[1])])
        else:
            print('** no instance found **')

    def do_destroy(self, arg):
        """Delete an instance class name and id and save in JSON"""
        arg_split = arg.split()
        if len(arg_split) == 0:
            print('** class name missing **')
        elif arg_split[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_split) == 1:
            print('** instance id missing **')
        elif "{}.{}".format(arg_split[0], arg_split[1]) in dic_obj.keys():
            del dic_obj["{}.{}".format(arg_split[0], arg_split[1])]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all string of all instances"""
        arg_split = arg.split()
        out_string = []

        if len(arg_split) == 0:
            for obj in dic_obj.values():
                out_string.append(obj.__str__())
            print(out_string)
        elif arg_split[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for obj in dic_obj.values():
                if arg_split[0] == obj.__class__.__name__:
                    out_string.append(obj.__str__())
            print(out_string)

    def do_update(self, arg):
        """Update instance class name and id and update is save in JSON"""
        arg_split = arg.split()
        if len(arg_split) == 0:
            print('** class name missing **')
        elif arg_split[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_split) == 1:
            print('** instance id missing **')
        elif "{}.{}".format(arg_split[0], arg_split[1]) not in dic_obj.keys():
            print('** no instance found **')
        elif len(arg_split) == 2:
            print('** attribute name missing **')
        elif len(arg_split) == 3:
            print('** value missing **')
        else:
            f_key = "{}.{}".format(arg_split[0], arg_split[1])
            try:
                setattr(dic_obj[f_key], arg_split[2], eval(arg_split[3]))
            except:
                setattr(dic_obj[f_key], arg_split[2], arg_split[3])
            models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
