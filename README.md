# Car Sales API

A FastAPI application for managing car sales and customer communications. This API provides endpoints for managing car listings and tracking customer communications about specific vehicles.

## Overview

The Car Sales API allows you to:
- Manage car listings (create and retrieve)
- Track customer communications about specific cars
- Handle relationships between cars and communications

## Prerequisites

- Docker installed on your system
- Make (usually pre-installed on Unix-based systems)

## Quick Start with Docker

The application is containerized using Docker for easy setup and deployment.

1. Setup the environment:
```bash
make setup
```

2. Build and run the application:
```bash
make run
```

The API will be available at `http://localhost:8000`

### Available Make Commands

- `make setup` - Create necessary directories with proper permissions
- `make build` - Build Docker image
- `make run` - Build and run Docker container
- `make stop` - Stop and remove Docker container
- `make clean` - Stop container and remove image
- `make test` - Run API endpoint tests
- `make help` - Show available commands

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

## Data Persistence

The application uses SQLite for data storage. The database file is stored in a Docker volume at `/data/db` for persistence between container restarts.

## Development

For development purposes, the application uses:
- FastAPI for the web framework
- SQLAlchemy for database ORM
- Pydantic for data validation
- Docker for containerization

## Testing

You can run the basic API tests using:
```bash
make test
```

This will:
1. Start the application if not running
2. Run a series of curl commands to test the main endpoints
3. Display the results

## Cleanup

To stop the application and clean up resources:
```bash
make clean
```

This will stop the container and remove the Docker image.
