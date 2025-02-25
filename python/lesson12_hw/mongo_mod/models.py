"""
Data models for products and orders.
"""

from datetime import datetime
from typing import List, Dict


def get_sample_products() -> List[Dict]:
    """Returns sample product data."""
    return [
        {"name": "Product1", "price": 2007, "category": "phones",
         "stock": 1000},
        {"name": "Product2", "price": 1150, "category": "phones",
         "stock": 1000},
        {"name": "Product3", "price": 2503, "category": "laptops",
         "stock": 2000},
        {"name": "Product4", "price": 4523, "category": "laptops",
         "stock": 500},
        {"name": "Product5", "price": 923, "category": "laptops",
         "stock": 400},
        {"name": "Product6", "price": 5554, "category": "mfu", "stock": 250},
        {"name": "Product7", "price": 1023, "category": "mfu", "stock": 100},
    ]


def get_sample_orders() -> List[Dict]:
    """Returns sample order data."""
    return [
        {
            "order_number": "ORD12345",
            "client_id": 2007,
            "products": [
                {"name": "Product1", "quantity": 2},
                {"name": "Product2", "quantity": 1},
            ],
            "total_amount": 5164,
            "date": datetime.now(),
        }
    ]
