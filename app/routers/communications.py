# communications.py
"""
Router module for communication-related endpoints.
Handles creation and retrieval of customer communications with proper error handling
and car relationship validation.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from .. import models, schemas

router = APIRouter(
    prefix="/communications",
    tags=["communications"]
)

@router.post("/", response_model=schemas.CommunicationOut, status_code=201)
def create_communication(comm: schemas.CommunicationCreate, db: Session = Depends(get_db)):
    """Log a new communication tied to a car"""
    try:
        # Check if the referenced car exists
        car = db.query(models.Car).filter(models.Car.id == comm.car_id).first()
        if not car:
            raise HTTPException(
                status_code=404,
                detail=f"Car with id {comm.car_id} not found"
            )
            
        db_comm = models.Communication(**comm.dict())
        db.add(db_comm)
        db.commit()
        db.refresh(db_comm)
        return db_comm
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Failed to create communication. Please check your input."
        )

@router.get("/{comm_id}", response_model=schemas.CommunicationOut)
def get_communication(comm_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific communication by its ID.
    
    Args:
        comm_id: Unique identifier of the communication
        db: Database session dependency
        
    Returns:
        CommunicationOut: Communication details if found
        
    Raises:
        HTTPException: If communication with given ID is not found (404)
    """
    db_comm = db.query(models.Communication).filter(models.Communication.id == comm_id).first()
    if db_comm is None:
        raise HTTPException(status_code=404, detail="Communication not found")
    return db_comm
