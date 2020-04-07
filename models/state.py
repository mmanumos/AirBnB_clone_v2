#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        name = ""

        @property
        def cities(self):
            city_list = []
            for value in models.storage.all(City).values():
                if value.state_id == self.id:
                    city_list.append(value)
            return city_list
