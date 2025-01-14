# Car Sales API

A FastAPI application for managing car sales and customer communications. This API provides endpoints for managing car listings and tracking customer communications about specific vehicles.

## Overview

The Car Sales API allows you to:
- Manage car listings (create and retrieve)
- Track customer communications about specific cars
- Handle relationships between cars and communications

## Installation

This project uses Poetry for dependency management. Make sure you have Python 3.10 or higher installed.

1. Install Poetry (if not already installed):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Clone the repository and install dependencies:
```bash
cd fastapi_car_sales
poetry install
```

## Dependencies

- fastapi==0.95.2
- uvicorn==0.22.0
- sqlalchemy==1.4.46
- pydantic==1.10.7

## Running the Application

Start the development server:
```bash
poetry run uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Cars

#### Create a Car Listing
- **POST** `/cars`
- **Request Body**:
```json
{
    "make": "Toyota",
    "model": "Camry",
    "year": 2022,
    "price": 25000.00
}
```
- **Response** (201 Created):
```json
{
    "id": 1,
    "make": "Toyota",
    "model": "Camry",
    "year": 2022,
    "price": 25000.00
}
```

#### Get Car Details
- **GET** `/cars/{car_id}`
- **Response** (200 OK):
```json
{
    "id": 1,
    "make": "Toyota",
    "model": "Camry",
    "year": 2022,
    "price": 25000.00
}
```

### Communications

#### Create a Communication
- **POST** `/communications`
- **Request Body**:
```json
{
    "customer_name": "John Doe",
    "customer_email": "john@example.com",
    "message": "Interested in this car. Please contact me.",
    "car_id": 1
}
```
- **Response** (201 Created):
```json
{
    "id": 1,
    "customer_name": "John Doe",
    "customer_email": "john@example.com",
    "message": "Interested in this car. Please contact me.",
    "car_id": 1
}
```

#### Get Communication Details
- **GET** `/communications/{comm_id}`
- **Response** (200 OK):
```json
{
    "id": 1,
    "customer_name": "John Doe",
    "customer_email": "john@example.com",
    "message": "Interested in this car. Please contact me.",
    "car_id": 1
}
```

## Error Handling

The API returns appropriate HTTP status codes:
- 201: Resource created successfully
- 200: Request successful
- 404: Resource not found
- 400: Bad request (validation error)

## Database

The application uses SQLite for data storage. The database file `car_sales.db` will be created automatically when you first run the application.
