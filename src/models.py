import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    fav_char = Column(Integer, ForeignKey("FavoritesChar.id")) #many to one
    fav_planet = Column(Integer, ForeignKey("FavoritesPlanet.id"))#many to one

class FavoritesChar(Base):
    __tablename__ = "favoriteschar"

    id = Column(Integer, primary_key=True)
    char_id = Column(Integer, ForeignKey("Character.id")) #many to one

class favoritesPlanet(Base):
    __tablename__ = "favoritesPlanet"

    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey("Planet.id")) #many to one

class Character(Base):
    __tablename__ = "character"

    id = Column(Integer, primary_key=True)
    name = Column(String(250),nullable=False)
    birth_year = Column(Integer)
    gender = Column(String(25))
    height = Column(Integer)
    skin_color = Column(String(25))

class Planet(Base):
    __tablename__ = "planet"

    id = Column(Integer, primary_key=True)
    name = Column(String(250),nullable=False)
    climate = Column(String(25))
    gravity = Column(Integer)
    population = Column(Integer)
    terrain = Column(String(25))



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
