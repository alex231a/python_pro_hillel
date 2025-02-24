"""Module with examples working with mongodb"""

from datetime import datetime, timedelta
from typing import List, Dict

from pymongo import MongoClient # type: ignore
from pymongo.collection import Collection # type: ignore
from pymongo.database import Database # type: ignore

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db: Database = client["online_store"]

# Create collections
products_collection: Collection = db["products"]
orders_collection: Collection = db["orders"]

# Insert sample products
products: List[Dict] = [
    {"name": "Product1", "price": 2007, "category": "phones", "stock": 1000},
    {"name": "Product2", "price": 1150, "category": "phones", "stock": 1000},
    {"name": "Product3", "price": 2503, "category": "laptops", "stock": 2000},
    {"name": "Product4", "price": 4523, "category": "laptops", "stock": 500},
    {"name": "Product5", "price": 923, "category": "laptops", "stock": 400},
    {"name": "Product6", "price": 5554, "category": "mfu", "stock": 250},
    {"name": "Product7", "price": 1023, "category": "mfu", "stock": 100},
]
products_collection.insert_many(products)

# Insert sample orders
orders: List[Dict] = [
    {
        "order_number": "ORD12345",
        "client_id": 2007,
        "products": [
            {"name": "Product1", "quantity": 2},
            {"name": "Product2", "quantity": 1}
        ],
        "total_amount": 5164,
        "date": datetime.now()
    }
]
orders_collection.insert_many(orders)

# Read all orders from the last 30 days
date_threshold = datetime.utcnow() - timedelta(days=30)
recent_orders = orders_collection.find({"date": {"$gte": date_threshold}})
print("Orders in the last 30 days:")
for order in recent_orders:
    print(order)


# Update stock after purchase
def update_stock(ord_er: Dict) -> None:
    """update order"""
    for item in ord_er["products"]:
        products_collection.update_one(
            {"name": item["name"]},
            {"$inc": {"stock": -item["quantity"]}}
        )


for order in orders:
    update_stock(order)

# Delete products that are out of stock
products_collection.delete_many({"stock": {"$lte": 0}})

# Aggregation: Total quantity of sold products in the last 30 days
pipeline = [
    {"$match": {"date": {"$gte": date_threshold}}},
    {"$unwind": "$products"},
    {"$group": {"_id": "$products.name",
                "total_sold": {"$sum": "$products.quantity"}}}
]
sales_report = orders_collection.aggregate(pipeline)
print("Total quantity of sold products:")
for report in sales_report:
    print(report)

# Aggregation: Total amount spent by a client
CLIENT_ID = 2007
pipeline = [
    {"$match": {"client_id": CLIENT_ID}},
    {"$group": {"_id": "$client_id", "total_spent": {"$sum": "$total_amount"}}}
]
total_spent = list(orders_collection.aggregate(pipeline))
print(
    f"Total amount spent by client {CLIENT_ID}: "
    f"{total_spent[0]['total_spent'] if total_spent else 0}")

# Create an index on category for faster queries
products_collection.create_index("category")
