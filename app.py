"""
E-commerce API Application
Simple Flask-based REST API for the trusted supply chain demo
"""

import os
import json
import logging
from datetime import datetime
from flask import Flask, jsonify, request

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# In-memory data store for demo
products = [
    {"id": 1, "name": "Laptop", "price": 999.99, "stock": 50},
    {"id": 2, "name": "Keyboard", "price": 79.99, "stock": 100},
    {"id": 3, "name": "Mouse", "price": 29.99, "stock": 200},
    {"id": 4, "name": "Monitor", "price": 299.99, "stock": 30},
    {"id": 5, "name": "Headphones", "price": 149.99, "stock": 75},
]

orders = []


@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint for Kubernetes probes"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": os.getenv("APP_VERSION", "1.0.0")
    })


@app.route("/ready", methods=["GET"])
def readiness_check():
    """Readiness check endpoint"""
    return jsonify({"status": "ready"})


@app.route("/", methods=["GET"])
def index():
    """Root endpoint"""
    return jsonify({
        "service": "ecommerce-api",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "endpoints": [
            "/health",
            "/ready",
            "/api/products",
            "/api/orders"
        ]
    })


@app.route("/api/products", methods=["GET"])
def get_products():
    """Get all products"""
    logger.info("Fetching all products")
    return jsonify({"products": products, "count": len(products)})


@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    """Get a specific product by ID"""
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404


@app.route("/api/orders", methods=["GET"])
def get_orders():
    """Get all orders"""
    return jsonify({"orders": orders, "count": len(orders)})


@app.route("/api/orders", methods=["POST"])
def create_order():
    """Create a new order"""
    data = request.get_json()
    
    if not data or "product_id" not in data or "quantity" not in data:
        return jsonify({"error": "Missing required fields: product_id, quantity"}), 400
    
    product = next((p for p in products if p["id"] == data["product_id"]), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    if product["stock"] < data["quantity"]:
        return jsonify({"error": "Insufficient stock"}), 400
    
    # Create order
    order = {
        "id": len(orders) + 1,
        "product_id": data["product_id"],
        "product_name": product["name"],
        "quantity": data["quantity"],
        "total": product["price"] * data["quantity"],
        "status": "pending",
        "created_at": datetime.utcnow().isoformat()
    }
    
    # Update stock
    product["stock"] -= data["quantity"]
    orders.append(order)
    
    logger.info(f"Order created: {order['id']}")
    return jsonify(order), 201


@app.route("/api/orders/<int:order_id>", methods=["GET"])
def get_order(order_id):
    """Get a specific order by ID"""
    order = next((o for o in orders if o["id"] == order_id), None)
    if order:
        return jsonify(order)
    return jsonify({"error": "Order not found"}), 404


@app.route("/metrics", methods=["GET"])
def metrics():
    """Simple metrics endpoint"""
    return jsonify({
        "total_products": len(products),
        "total_orders": len(orders),
        "total_revenue": sum(o["total"] for o in orders)
    })


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    debug = os.getenv("DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)
