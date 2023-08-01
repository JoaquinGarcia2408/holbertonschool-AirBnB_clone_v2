#!/usr/bin/python3
"""Defines a class to manage file storage."""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary __objects"""
        if cls is None:
            return self.__objects
        else:
            dic_objects = {}
            for key, value in self.__objects.items():
                if isinstance(value, cls):
                    dic_objects[key] = value
            return dic_objects

    def new(self, obj):
        """Adds a new object to the storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves the storage dictionary to a file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads the storage dictionary from a file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete objects"""
        if obj is not None:
            del_obj = "{}.{}".format(obj.__class__.__name__, obj.id)
            if del_obj in self.__objects:
                del self.__objects[del_obj]
        else:
            pass
