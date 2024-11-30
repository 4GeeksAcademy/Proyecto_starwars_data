import os
import sys
from sqlalchemy import Column, Integer, String, ForeignKey,Enum
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

# Base declarativa para los modelos
Base = declarative_base()

# Tabla de usuarios
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)

    # (to_dict): Útil para transformar datos a JSON u otros formatos
    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email
        }

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    hair_color = Column(String(50))
    eye_color = Column(String(50))
    gender = Column(Enum("Male","Female", "Other", name="gender_enum"))
    species = Column(String(50))
    height = Column(Integer)

    def to_dift(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "heir_color" : self.heir_color,
            "eye_color" : self.eye_color,
            "gender" : self.gender,
            "species" : self.species,
            "height" : self.height,
        }
    
# Tabla de planetas
class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    terrain = Column(String(50))
    population = Column(Integer)
    climate = Column (String(50))
    gravity = Column (String(50))

    def to_dilf(self):
        return{
            "id": self.id,
            "name": self.name,
            "terrain": self.terrain,
            "population": self.population,
            "climate": self.climate,
            "gravity": self.gravity,
        }
        
# Tabla de vehículos
class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    _class = Column(String(50))
    passenger = Column(Integer)
    model = Column(String(50))
    max_speed = Column(Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "vehicle_class": self.vehicle_class,
            "passenger": self.passenger,
            "model": self.model,
            "max_speed": self.max_speed,
        }

# Tablas de favoritos específicas
class CharacterFavorit(Base):
    __tablename__ = 'character_favorit'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    user = relationship(User)
    character = relationship(Character)

class PlanetFavorit(Base):
    __tablename__ = 'planet_favorit'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    user = relationship(User)
    planet = relationship(Planet)

class VehicleFavorit(Base):
    __tablename__ = 'vehicle_favorit'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    user = relationship(User)
    vehicle = relationship(Vehicle)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')