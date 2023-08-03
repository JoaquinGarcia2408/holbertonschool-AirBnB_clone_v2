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
from os import environ

modelos = {"User": User, "State": State,
           "City": City, "Amenity": Amenity,
           "Place": Place, "Review": Review}

class DBStorage():
    """Placeholder"""
    __engine = None
    __session = None

    def __init__(self):
        user = environ.get('HBNB_MYSQL_USER')
        pw = environ.get('HBNB_MYSQL_PWD')
        ht = environ.get('HBNB_MYSQL_HOST')
        db = environ.get('HBNB_MYSQL_DB')
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{pw}@{ht}/{db}',
                                      pool_pre_ping=True)
        if environ.get("HBNB_ENV") == "test":
            Base.metadata.drop(self.__engine)

    def all(self, cls=None):
        objects = {}
        for clas in modelos:
            if modelos[clas] == cls or cls is None:
                for key in self.__session.query(modelos[clas]).all():
                    key = "{}.{}".format(__name__+'.'+key.id)
        return objects

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """comments"""
        self.__session.delete(obj)

    def reload(self):
        """comments"""
        Base.metadata.create_all(self.__engine)
        ssession = sessionmaker(bind=self.__engine, expire_on_commit=False)
        ssession = scoped_session(ssession)
        self.__session = ssession

    def close(self):
        """comments"""
        self.__session.close()
