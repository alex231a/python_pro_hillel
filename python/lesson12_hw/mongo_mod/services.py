"""
Service functions for business logic.
"""

from datetime import datetime, timedelta

from db_manager import MongoDBManager


def get_recent_orders(database: MongoDBManager, days: int = 30):
    """Fetch orders from the last 'days' days."""
    date_threshold = datetime.utcnow() - timedelta(days=days)
    return list(database.orders_collection.find({"date": {"$gte": date_threshold}}))


def get_sales_report(database: MongoDBManager, days: int = 30):
    """Returns sales report for the last 'days' days."""
    date_threshold = datetime.utcnow() - timedelta(days=days)
    pipeline = [
        {"$match": {"date": {"$gte": date_threshold}}},
        {"$unwind": "$products"},
        {"$group": {"_id": "$products.name",
                    "total_sold": {"$sum": "$products.quantity"}}},
    ]
    return list(database.orders_collection.aggregate(pipeline))


def get_total_spent_by_client(database: MongoDBManager, client_id: int):
    """Returns total amount spent by a specific client."""
    pipeline = [
        {"$match": {"client_id": client_id}},
        {"$group": {"_id": "$client_id",
                    "total_spent": {"$sum": "$total_amount"}}},
    ]
    result = list(database.orders_collection.aggregate(pipeline))
    return result[0]["total_spent"] if result else 0
