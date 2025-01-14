# cars.py
"""
Router module for car-related endpoints.
Handles creation and retrieval of car listings with proper error handling.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from .. import models, schemas

router = APIRouter(
    prefix="/cars",
    tags=["cars"]
)

@router.post("/", response_model=schemas.CarOut, status_code=201)
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    """Add a new car listing"""
    try:
        db_car = models.Car(**car.dict())
        db.add(db_car)
        db.commit()
        db.refresh(db_car)
        return db_car
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Failed to create car listing. Please check your input."
        )

@router.get("/{car_id}", response_model=schemas.CarOut)
def get_car(car_id: int, db: Session = Depends(get_db)):
    """
    Retrieve details of a car by its ID.
    
    Args:
        car_id: Unique identifier of the car
        db: Database session dependency
        
    Returns:
        CarOut: Car details if found
        
    Raises:
        HTTPException: If car with given ID is not found (404)
    """
    db_car = db.query(models.Car).filter(models.Car.id == car_id).first()
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car
