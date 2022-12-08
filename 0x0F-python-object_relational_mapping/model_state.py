#!/usr/bin/python3
""" Defines a State class that links to table states
-has class attribute id that represents a column of an auto-generated
unique integer, can’t be null and is a primary key
-class attribute name that represents a column of a string with maximum
128 characters and can’t be null
"""


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    '''represents State in mysql DB'''

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
