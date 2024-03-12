#!/usr/bin/python3

"""
get the cmd module
get datetime module
get the BaseModel
get shlex module to split the arguments in a way that
    handles double-quoted values correctly
"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime
import shlex
import sys
import re

"""
class HBNBCommand console

create -> use comand create (<className>)
view -> use comand show (<className> <instanceId>)
view all -> use comand all
update -> use comand update (<className> <instanceId> <attrName> <attrValue>)
delete -> use comand destroy (<className> <instanceId>)

exit -> use comand quit
"""


class HBNBCommand(cmd.Cmd):

    """ prompt to be shown when the console starts """
    prompt = '(hbnb) '
    classes = ['BaseModel', 'User', 'State', 'City',
               'Amenity', 'Place', 'Review']

    def do_EOF(self, line):
        """ function to exit from the console """
        return True

    def do_quit(self, line):
        """ function to exit from the console """
        return True

    def emptyline(self):
        """
        empty line should do nothing
        Dont execute the previous command when line is empty
        """
        pass

    def do_create(self, line):
        """
        Creates a new instance of <className> and saves it to file.JSON
        prints the instance id
        command is:-> create <className>

        if <className> not provided
        prints: ** class name missing **

        if <className> is wrong
        prints: ** class doesn't exist **
        """
        className = self.parseline(line)[0]
        if not className or className is None:
            print("** class name missing **")
            return
        elif className not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        else:
            my_model = eval(className)()
            my_model.save()
            print(my_model.id)

    def do_show(self, line):
        """
        show retrives an instance of <className>
        prints the instance
        command is:-> show <className> <instanceId>

        if <className> not provided
        prints: ** class name missing **

        if <className> is wrong
        prints: ** class doesn't exist **

        if <instanceId> is wrong
        prints: ** no instance found **
        """
        className = self.parseline(line)[0]
        classId = self.parseline(line)[1]
        if not className:
            print("** class name missing **")
            return
        elif className not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        else:
            if not classId:
                print("** instance id missing **")
                return
            else:
                inst_key = f"{className}.{classId}"
                inst_data = models.storage.all().get(inst_key)
                if inst_data is None:
                    print('** no instance found **')
                    return
                else:
                    print(inst_data)

    def do_destroy(self, line):
        """
        destroy destroys an instance of <className> and
        save changes to json file
        command is:-> destroy <className> <instanceId>

        if <className> not provided
        prints: ** class name missing **

        if <className> is wrong
        prints: ** class doesn't exist **

        if <instanceId> is wrong
        prints: ** no instance found **
        """
        className = self.parseline(line)[0]
        classId = self.parseline(line)[1]
        if not className:
            print("** class name missing **")
            return
        elif className not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        else:
            if not classId:
                print("** instance id missing **")
                return
            else:
                inst_key = f"{className}.{classId}"
                inst_data = models.storage.all().get(inst_key)
                if inst_data is None:
                    print('** no instance found **')
                    return
                else:
                    del (models.storage.all())[inst_key]
                    models.storage.save()

    def do_all(self, line):
        """
        all command prints all string rep of all instances bases on
        <className> provided or only all command still prints
        if class does not exists ptints(** class doesn't exist **)
        """
        className = self.parseline(line)[0]
        if className and className not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        else:
            # select all instance
            instances = models.storage.all()
        if className:
            # get all instance of same className
            filtered_instances = {key: instance for key, instance
                                  in instances.items() if className in key}
        else:
            # get all the instaces that exist
            filtered_instances = instances
        # print found instances as a list
        print([str(instance) for instance in filtered_instances.values()])

    def do_update(self, line):
        """
        update command updates an instance based on the className and id
        by adding or updating atribute then save changes into a json file.

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Updates an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instances = models.storage.all()
        instance_key = "{}.{}".format(class_name, args[1])
        if instance_key not in instances:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]

        # Handle attribute values enclosed in double quotes
        if attribute_value.startswith('"') and attribute_value.endswith('"'):
            attribute_value = attribute_value[1:-1]

        instance = instances[instance_key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def get_objects(self, value):
        """
        Retrieves instances by class name
        """
        if value:
            instances = models.storage.all()
            # get all instance of same className
            filtered_instances = {key: instance for key, instance
                                  in instances.items() if value in key}
            return [str(instance) for instance in filtered_instances.values()]

    def cleanWord(self, word):
        """
        check if word contains " or , and remove them
        """
        if word and (',' in word or '"' in word):
            newWord = ''
            for char in word:
                if char == '"' or char == ',':
                    newWord = newWord + ''
                else:
                    newWord = newWord + char
            return newWord
        else:
            return word

    def default(self, line):
        """
        When the command prefix is not recognized, this method
        looks for whether the command entered has the syntax:
        "<class name>.<method name>" or not,
        and links it to the corresponding method in case the
        class exists and the method belongs to the class.

        """
        if '.' in line:
            splitted = re.split(r'\.|\(|\)', line)
            class_name = splitted[0]
            method_name = splitted[1]

            if class_name in HBNBCommand.classes:
                if method_name == 'all':
                    print(self.get_objects(class_name))
                elif method_name == 'count':
                    print(len(self.get_objects(class_name)))
                elif method_name == 'show':
                    instance_id = splitted[2][1:-1]
                    self.do_show(class_name + ' ' + instance_id)
                elif method_name == 'destroy':
                    instance_id = splitted[2][1:-1]
                    self.do_destroy(class_name + ' ' + instance_id)
                elif method_name == 'update':
                    instance_data = splitted[2].split(' ')
                    instance_id = self.cleanWord(instance_data[0])
                    attrName = self.cleanWord(instance_data[1])
                    attrValue = self.cleanWord(instance_data[2])
                    self.do_update(class_name + ' ' + instance_id
                                   + ' ' + attrName + ' ' + attrValue)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
