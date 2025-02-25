"""
Main module to run the application.
"""

from db_manager import MongoDBManager
from models import get_sample_products, get_sample_orders
from services import get_recent_orders, get_sales_report, \
    get_total_spent_by_client

if __name__ == "__main__":
    # Initialize database manager
    db_manager = MongoDBManager()

    # Insert sample data
    db_manager.insert_products(get_sample_products())
    db_manager.insert_orders(get_sample_orders())

    # Process orders (update stock)
    for order in get_sample_orders():
        db_manager.update_stock(order)

    # Remove out-of-stock products
    db_manager.remove_out_of_stock_products()

    # Generate reports
    print("Orders in the last 30 days:")
    for order in get_recent_orders(db_manager):
        print(order)

    print("Total quantity of sold products:")
    for report in get_sales_report(db_manager):
        print(report)

    CLIENT_ID = 2007
    print(
        f"Total amount spent by client {CLIENT_ID}: "
        f"{get_total_spent_by_client(db_manager, CLIENT_ID)}")

    # Create indexes
    db_manager.create_indexes()
