#!/usr/bin/python3
"""Base.py"""
import json


class Base:
    """ Define a private attribute """
    __nb_objects = 0
    """ Class constructor"""
    def __init__(self, id=None):
        """
            Initialize an instance abd verify if id is None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Convert a list of dictionaries to Json format """
        if not list_dictionaries:
            return "[]"

        json_data = json.dumps(list_dictionaries)
        return json_data

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Convert list_objs to json format and save to
            a file with a .json extension.
        """
        if list_objs is None:
            list_objs = []

        name_class = cls.__name__ + '.json'
        dict_list = []

        for obj in list_objs:
            dictionary_element = obj.to_dictionary()
            dict_list.append(dictionary_element)

        json_data = cls.to_json_string(dict_list)
        with open(name_class, "w") as file:
            file.write(json_data)

    @staticmethod
    def from_json_string(json_string):
        """ Convert Json format to a object (dictionary - key and value) """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            Return a instance with all atributes initialized.
        """

        """I need a instance before to call update function"""
        dummy_instance = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        name_class = cls.__name__ + '.json'
        instance_list = []
        try:
            with open(name_class, "r") as file:
                json_data = file.read()
                if json_data:
                    dictionary_data = cls.from_json_string(json_data)
                    for dictionary in dictionary_data:
                        instance = cls.create(**dictionary)
                        instance_list.append(instance)
        except FileNotFoundError:
            return []
        return instance_list
