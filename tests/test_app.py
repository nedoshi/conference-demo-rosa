"""
Unit tests for E-commerce API
"""

import pytest
import json
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app


@pytest.fixture
def client():
    """Create test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestHealthEndpoints:
    """Test health check endpoints"""
    
    def test_health_check(self, client):
        """Test /health endpoint returns healthy status"""
        response = client.get('/health')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['status'] == 'healthy'
        assert 'timestamp' in data
        assert 'version' in data
    
    def test_readiness_check(self, client):
        """Test /ready endpoint returns ready status"""
        response = client.get('/ready')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['status'] == 'ready'
    
    def test_index(self, client):
        """Test root endpoint returns service info"""
        response = client.get('/')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['service'] == 'ecommerce-api'
        assert 'endpoints' in data


class TestProductEndpoints:
    """Test product endpoints"""
    
    def test_get_products(self, client):
        """Test GET /api/products returns product list"""
        response = client.get('/api/products')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'products' in data
        assert 'count' in data
        assert data['count'] > 0
    
    def test_get_product_by_id(self, client):
        """Test GET /api/products/<id> returns specific product"""
        response = client.get('/api/products/1')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['id'] == 1
        assert 'name' in data
        assert 'price' in data
    
    def test_get_product_not_found(self, client):
        """Test GET /api/products/<id> returns 404 for invalid ID"""
        response = client.get('/api/products/9999')
        assert response.status_code == 404
        data = json.loads(response.data)
        assert 'error' in data


class TestOrderEndpoints:
    """Test order endpoints"""
    
    def test_get_orders(self, client):
        """Test GET /api/orders returns order list"""
        response = client.get('/api/orders')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'orders' in data
        assert 'count' in data
    
    def test_create_order(self, client):
        """Test POST /api/orders creates new order"""
        order_data = {
            'product_id': 1,
            'quantity': 2
        }
        response = client.post(
            '/api/orders',
            data=json.dumps(order_data),
            content_type='application/json'
        )
        assert response.status_code == 201
        data = json.loads(response.data)
        assert data['product_id'] == 1
        assert data['quantity'] == 2
        assert 'total' in data
        assert data['status'] == 'pending'
    
    def test_create_order_missing_fields(self, client):
        """Test POST /api/orders returns 400 for missing fields"""
        response = client.post(
            '/api/orders',
            data=json.dumps({}),
            content_type='application/json'
        )
        assert response.status_code == 400
    
    def test_create_order_invalid_product(self, client):
        """Test POST /api/orders returns 404 for invalid product"""
        order_data = {
            'product_id': 9999,
            'quantity': 1
        }
        response = client.post(
            '/api/orders',
            data=json.dumps(order_data),
            content_type='application/json'
        )
        assert response.status_code == 404


class TestMetricsEndpoint:
    """Test metrics endpoint"""
    
    def test_metrics(self, client):
        """Test /metrics endpoint returns metrics"""
        response = client.get('/metrics')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'total_products' in data
        assert 'total_orders' in data
        assert 'total_revenue' in data
