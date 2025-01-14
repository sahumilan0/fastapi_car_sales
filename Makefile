.PHONY: help setup build run stop clean test

# Variables
CONTAINER_NAME = car-sales-container
IMAGE_NAME = car-sales-api
PORT = 8000
DATA_DIR = data/db

help:
	@echo "FastAPI Car Sales API Makefile"
	@echo ""
	@echo "Usage:"
	@echo "  make setup     - Create necessary directories with proper permissions"
	@echo "  make build     - Build Docker image"
	@echo "  make run       - Run Docker container"
	@echo "  make stop      - Stop and remove Docker container"
	@echo "  make clean     - Stop container and remove image"
	@echo "  make test      - Run API endpoint tests"
	@echo ""

setup:
	@echo "Creating data directory..."
	sudo mkdir -p $(DATA_DIR)
	sudo chmod -R 777 data

build:
	@echo "Building Docker image..."
	docker build -t $(IMAGE_NAME) .

run: setup build
	@echo "Running Docker container..."
	docker rm -f $(CONTAINER_NAME) 2>/dev/null || true
	docker run -d --name $(CONTAINER_NAME) \
		-p $(PORT):$(PORT) \
		-v $$(pwd)/$(DATA_DIR):/data/db \
		$(IMAGE_NAME)
	@echo "Container started! API available at http://localhost:$(PORT)"
	@echo "Waiting for application to start..."
	sleep 5

stop:
	@echo "Stopping Docker container..."
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true

clean: stop
	@echo "Removing Docker image..."
	docker rmi $(IMAGE_NAME) || true

test: run
	@echo "\nTesting Car Creation..."
	curl -L -X POST http://localhost:$(PORT)/cars/ \
		-H "Content-Type: application/json" \
		-d '{"make":"Toyota","model":"Camry","year":2022,"price":25000.00}'

	@echo "\n\nTesting Car Retrieval..."
	curl -L http://localhost:$(PORT)/cars/1

	@echo "\n\nTesting Communication Creation..."
	curl -L -X POST http://localhost:$(PORT)/communications/ \
		-H "Content-Type: application/json" \
		-d '{"customer_name":"John Doe","customer_email":"john@example.com","message":"Interested in this car","car_id":1}'

	@echo "\n\nTesting Communication Retrieval..."
	curl -L http://localhost:$(PORT)/communications/1
	@echo "\n"
