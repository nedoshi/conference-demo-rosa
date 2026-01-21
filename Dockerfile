FROM registry.access.redhat.com/ubi9/python-311:latest

LABEL name="ecommerce-api" \
      version="1.0.0" \
      description="E-commerce API for Trusted Supply Chain Demo" \
      maintainer="demo@example.com"

# Set working directory
WORKDIR /opt/app-root/src

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .
COPY tests/ tests/

# Set environment variables
ENV PORT=8080 \
    APP_VERSION=1.0.0 \
    PYTHONUNBUFFERED=1

# Expose port
EXPOSE 8080

# Run with gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "--threads", "4", "app:app"]
