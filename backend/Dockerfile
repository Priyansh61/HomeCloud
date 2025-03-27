FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy only requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set Python path so `app.*` imports work
ENV PYTHONPATH=/app

# Run with hot reload
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--reload-dir", "app", "--reload-delay", "0.5", "--reload-include", "*.py"]
