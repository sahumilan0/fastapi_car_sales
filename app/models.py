# models.py
"""
SQLAlchemy models for the Car Sales API.
Defines the database schema and relationships between tables.
"""

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Car(Base):
    """Car model representing vehicle listings in the database."""
    __tablename__ = "cars"

    # Primary key and indexed columns for efficient querying
    id = Column(Integer, primary_key=True, index=True)
    make = Column(String, index=True)  # Car manufacturer
    model = Column(String, index=True)  # Car model name
    year = Column(Integer)  # Manufacturing year
    price = Column(Float)  # Vehicle price

    # One-to-many relationship: one car can have multiple communications
    communications = relationship("Communication", back_populates="car")

class Communication(Base):
    """Communication model representing customer messages about specific cars."""
    __tablename__ = "communications"

    # Primary key and basic fields
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String)  # Name of the customer
    customer_email = Column(String)  # Customer's email address
    message = Column(String)  # Content of the communication
    car_id = Column(Integer, ForeignKey("cars.id"))  # Reference to associated car

    # Many-to-one relationship: many communications can reference one car
    car = relationship("Car", back_populates="communications")
