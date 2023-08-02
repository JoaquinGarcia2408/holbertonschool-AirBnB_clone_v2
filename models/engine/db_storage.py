#!/usr/bin/python3
from models.user import User
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from os import getenv

modelos = {"User": User, "State": State,
           "City": City, "Amenity": Amenity,
           "Place": Place, "Review": Review}

class DBStorage():
    """Placeholder"""
    __engine = None
    __session = None