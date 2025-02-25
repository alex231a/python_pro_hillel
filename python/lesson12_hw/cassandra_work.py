"""
Module for interacting with Apache Cassandra to store and manage event logs.

Features:
- Connect to a Cassandra cluster
- Create a keyspace and a table for event logs
- Perform CRUD operations (Create, Read, Update, Delete)
"""

import uuid
from datetime import datetime, timedelta

from cassandra.cluster import Cluster  # type: ignore

# Connect to Cassandra
cluster = Cluster(
    ['127.0.0.1'])  # Specify the IP address of the Cassandra node
session = cluster.connect()

# Create keyspace
session.execute("""
    CREATE KEYSPACE IF NOT EXISTS event_logs
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
""")

# Select keyspace
session.set_keyspace('event_logs')

# Create logs table
session.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        event_id UUID PRIMARY KEY,
        user_id TEXT,
        event_type TEXT,
        timestamp TIMESTAMP,
        metadata TEXT
    );
""")

print("Table logs created!")


# Function to add a new event
def add_event(user_id: str, event_type: str, metadata: str) -> None:
    """Insert a new event log into the Cassandra table."""
    event_id = uuid.uuid4()
    timestamp = datetime.utcnow()
    session.execute("""
        INSERT INTO logs (event_id, user_id, event_type, timestamp, metadata)
        VALUES (%s, %s, %s, %s, %s)
    """, (event_id, user_id, event_type, timestamp, metadata))
    print(f"Event added: {event_id}")


# Function to retrieve events from the last 24 hours
def get_recent_events(event_type: str) -> None:
    """Fetch all events of a given type from the last 24 hours."""
    since = datetime.utcnow() - timedelta(days=1)
    rows = session.execute("""
        SELECT * FROM logs WHERE event_type = %s AND timestamp >= %s ALLOW 
        FILTERING
    """, (event_type, since))

    for row in rows:
        print(
            f"Event ID: {row.event_id}, User: {row.user_id}, Time: "
            f"{row.timestamp}, Metadata: {row.metadata}")


# Function to update metadata for a specific event_id
def update_metadata(event_id: uuid.UUID, new_metadata: str) -> None:
    """Update the metadata field for a specific event."""
    session.execute("""
        UPDATE logs SET metadata = %s WHERE event_id = %s
    """, (new_metadata, event_id))
    print(f"Metadata updated for event_id: {event_id}")


# Function to delete old events (older than 7 days)
def delete_old_events() -> None:
    """Delete events that are older than 7 days."""
    threshold = datetime.utcnow() - timedelta(days=7)
    session.execute("""
        DELETE FROM logs WHERE timestamp < %s ALLOW FILTERING
    """, (threshold,))
    print("Old events (older than 7 days) deleted")


if __name__ == "__main__":
    add_event("user123", "login", "User logged in from IP 192.168.1.1")
    get_recent_events("login")
