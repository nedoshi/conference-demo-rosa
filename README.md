# E-commerce API

Simple Flask REST API for the Trusted Supply Chain Demo.

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py

# Run tests
pip install -r tests/requirements-test.txt
pytest tests/ -v
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/ready` | GET | Readiness check |
| `/api/products` | GET | List all products |
| `/api/products/<id>` | GET | Get product by ID |
| `/api/orders` | GET | List all orders |
| `/api/orders` | POST | Create new order |
| `/metrics` | GET | Application metrics |

## Build Container

```bash
podman build -t quay.io/flyers22/ecommerce-api:latest .
podman push quay.io/flyers22/ecommerce-api:latest
```
