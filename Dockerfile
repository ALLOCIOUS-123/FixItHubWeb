FROM python:3.11-slim

# Set environment variables
ENV FLASK_APP=app.py \
    FLASK_ENV=production \
    FLASK_DEBUG=0

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 5000

# Command to run the application
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]