# Use official Python image as base
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the requirements and install dependencies
COPY pyproject.toml poetry.lock ./
RUN pip install --no-cache-dir uv

# Copy the application code
COPY src/ .

# Expose the FastAPI port
EXPOSE 8000

# Start the FastAPI application
CMD ["uv", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]