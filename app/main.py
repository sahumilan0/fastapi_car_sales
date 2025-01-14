# main.py
"""
Entry point for the Car Sales API application.
Configures FastAPI app, includes routers, and sets up database tables.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from . import models  # Import models to register them with SQLAlchemy
from .routers import cars, communications

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Car Sales API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for this demo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(cars.router)
app.include_router(communications.router)

# Root endpoint
@app.get("/")
def read_root():
    """Root endpoint returning API information"""
    return {"message": "Welcome to Car Sales API", "version": "1.0.0"}
