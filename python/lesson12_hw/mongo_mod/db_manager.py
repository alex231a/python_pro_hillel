"""
Database manager module for MongoDB interactions.
"""

from pymongo import MongoClient # type: ignore
from pymongo.collection import Collection # type: ignore
from pymongo.database import Database # type: ignore

from config import MONGO_URI, DB_NAME


class MongoDBManager:
    """Handles MongoDB connections and operations."""

    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.database: Database = self.client[DB_NAME]
        self.products_collection: Collection = self.database["products"]
        self.orders_collection: Collection = self.database["orders"]

    def insert_products(self, products):
        """Insert multiple products into the database."""
        self.products_collection.insert_many(products)

    def insert_orders(self, orders):
        """Insert multiple orders into the database."""
        self.orders_collection.insert_many(orders)

    def update_stock(self, order):
        """Update product stock based on an order."""
        for item in order["products"]:
            self.products_collection.update_one(
                {"name": item["name"]}, {"$inc": {"stock": -item["quantity"]}}
            )

    def remove_out_of_stock_products(self):
        """Delete products that are out of stock."""
        self.products_collection.delete_many({"stock": {"$lte": 0}})

    def create_indexes(self):
        """Create indexes for faster queries."""
        self.products_collection.create_index("category")
