# schemas.py
"""
Pydantic models for request/response validation and serialization.
Defines the shape of data that the API accepts and returns.
"""

from pydantic import BaseModel
from typing import List, Optional

# Car schemas
class CarBase(BaseModel):
    make: str
    model: str
    year: int
    price: float

class CarCreate(CarBase):
    pass

class CarOut(CarBase):
    id: int

    class Config:
        orm_mode = True

# Communication schemas for request/response handling
class CommunicationBase(BaseModel):
    """Base Pydantic model for Communication with common attributes."""
    customer_name: str  # Customer's full name
    customer_email: str  # Customer's email address
    message: str  # Content of the communication
    car_id: int  # ID of the car this communication is about

class CommunicationCreate(CommunicationBase):
    """Schema for creating new communications (inherits all fields from CommunicationBase)."""
    pass

class CommunicationOut(CommunicationBase):
    """Schema for communication responses, includes database ID."""
    id: int  # Database-assigned ID

    class Config:
        orm_mode = True
