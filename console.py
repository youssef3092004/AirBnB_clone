#!/usr/bin/python3

import cmd
import shlex
from models import storage as st
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.review import Review

classes = {
    "BaseModel", BaseModel,
    "User", User,
    "Place", Place,
    "Review", Review,
    "State", State,
    "City", City,
    "Amenity", Amenity,
    "Review", Review,
    }

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand is a command-line interface for managing objects in the HBNB project.

    Attributes:
        prompt (str): The prompt string for the command line interface.

    Methods:
        do_quit(self, arg):
            Quit or exit the program.

        help_quit(self):
            Provide help information for the 'quit' command.

        do_EOF(self, arg):
            Handle the EOF (End Of File) event to exit the program.

        help_EOF(self):
            Provide help information for the EOF event.

        emptyline(self):
            Do nothing when an empty input line is encountered.

        do_create(self, class_name):
            Create a new instance of a class and save it.

        do_show(self, arg):
            Show details of a specific instance.

        do_destroy(self, arg):
            Destroy a specific instance.

        do_all(self, arg):
            List all instances or instances of a specific class.

        update(self, arg):
            Update attributes of a specific instance.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit or exit the program.

        Parameters:
            arg (str): The argument passed to the 'quit' command.

        Returns:
            bool: True if the command is executed successfully, False otherwise.
        """
        return True

    def do_EOF(self, arg):
        """
        Handle the EOF (End Of File) to exit the program.

        Parameters:
            arg (str): The argument passed to the EOF event.

        Returns:
            bool: True if the command is executed successfully, False otherwise.
        """
        print()
        return True

    def help_quit(self):
        """
        Provide help information for the 'quit' command.

        Returns:
            None: No return value.
        """
        print("Quit command to exit from the program")


    def help_EOF(self):
        """
        Provide help information for the EOF event.

        Returns:
            None: No return value.
        """
        print("EOF (Ctrl+D) to exit the program")

    def emptyline(self):
        """
        Do nothing on empty input line.

        Parameters:
            None: No parameters.

        Returns:
            None: No return value.
        """
        pass

    def do_create(self, class_name):
        """
        Create a new instance of a class and save it.

        Parameters:
            class_name (str): The name of the class to instantiate.

        Returns:
            None: No return value.
        """
        if not class_name:
            print("** class name missing **")
            return
        if class_name not in classes:
            print(f"** class doesn't exist **")
            return
        new_class = classes[class_name]()
        new_class.save()
        print(new_class.id)

    def do_show(self, arg):
        """
        Show details of a specific instance.

        Parameters:
            arg (str): The arguments passed to the command.

        Returns:
            None: No return value.
        """
        args = shlex.split(arg)
        class_name = args[0]
        class_id = args[1]
        if not class_name:
            print("** class name missing **")
            return
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if not class_id:
            print("** instance id missing **")
            return
        if class_id not in classes:
            print("** no instance found **")
            return
        s = ".".join(args)
        objects = st.all()
        if s not in objects.keys():
            print("** no instance found **")
            return
        print(objects[s].__str__())

    def do_destroy(self, arg):
        """
        Destroy a specific instance.

        Parameters:
            arg (str): The arguments passed to the command.

        Returns:
            None: No return value.
        """
        args = shlex.split(arg)
        class_name = args[0]
        class_id = args[1]
        if not class_name:
            print("** class name missing **")
            return
        if class_name not in classes:
            print(f"** class doesn't exist **")
            return
        if not class_id:
            print("** instance id missing **")
            return
        if class_id not in classes:
            print("** no instance found **")
            return
        s = ".".join(args)
        objects = st.all()
        if s not in objects.key():
            print("** no instance found **")
            return
        del objects[s]
        st.save()

    def do_all(self, arg):
        """
        List all instances or instances of a specific class.

        Parameters:
            arg (str): The arguments passed to the command.

        Returns:
            None: No return value.
        """
        objects = st.all()
        if not arg:
            temp = list()
            for key in objects:
                temp.append(objects[key].__str__())
                print(temp)
        else:
            if arg not in classes:
                print("** class doesn't exist **")
                return
            temp = list()
            for value in objects:
                temp.append(objects[value].__str__())
            if temp:
                print(temp)
    def update(self, arg):
        """
        Update attributes of a specific instance.

        Parameters:
            arg (str): The arguments passed to the command.

        Returns:
            None: No return value.
        """
        args = shlex.split(arg)
        class_name = args[0]
        class_id = args[1]
        attribute = args[2]
        value = args[3]
        if not class_name:
            print("** class name missing **")
            return
        if class_name not in classes:
            print(f"** class doesn't exist **")
            return
        if not class_id:
            print("** instance id missing **")
            return
        if class_id not in classes:
            print("** no instance found **")
            return
        if not attribute:
            print("** attribute name missing **")
            return
        if not value:
            print("** value missing **")
            return
        s = ".".join([class_name, class_id])
        objects = st.all()
        if s not in objects.keys():
            print("** no instance found **")
            return
        setattr(objects[s], attribute, value)
        st.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
