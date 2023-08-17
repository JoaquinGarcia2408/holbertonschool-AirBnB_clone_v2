#!/usr/bin/python3
<<<<<<< HEAD
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
=======
""" Stte Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
>>>>>>> bfe7d7a89ed3630949745f11107717c521a3196c
from os import getenv


class State(BaseModel, Base):
    """ State class """
<<<<<<< HEAD
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete-orphan')

    if (getenv("HBNB_TYPE_STORAGE") != "db"):
        @property
        def cities(self):
            from models import storage
            st_cities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    st_cities.append(city)
            return st_cities
=======
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state",
                              cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """Returns the list of City instances
            with state_id equals to the current State.id"""
            from models.city import City
            from models import storage
            listed = []
            for v in storage.all(City).values():
                if v.state_id == self.id:
                    listed.append(v)
            return listed
>>>>>>> bfe7d7a89ed3630949745f11107717c521a3196c
