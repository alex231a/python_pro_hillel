"""Module for working with Cassandra DB"""

# docker run --name cassandra -d -p 9042:9042 cassandra:latest - command to
# run Cassandra in Docker
# docker start cassandra
import uuid
from datetime import datetime, timedelta

from cassandra.cluster import Cluster  # type: ignore

# Connect to Cassandra
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()

# Create keyspace if it doesn't exist
session.execute("""
    CREATE KEYSPACE IF NOT EXISTS event_logs 
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
""")
session.set_keyspace('event_logs')

# Create the table with event_id as the PRIMARY KEY
session.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        event_id UUID PRIMARY KEY,
        user_id TEXT,
        event_type TEXT,
        timestamp TIMESTAMP,
        metadata TEXT
    );
""")

print("✅ Table 'logs' created!")


# Function to add a new event to the logs table
def add_event(user_id: str, event_type: str, metadata: str) -> uuid.UUID:
    """
    Adds a new event to the logs table.

    Args:
    - user_id (str): The ID of the user who performed the event.
    - event_type (str): The type of the event.
    - metadata (str): Additional data related to the event.

    Returns:
    - uuid.UUID: The ID of the newly created event.
    """
    event_id = uuid.uuid4()
    timestamp = datetime.utcnow()
    session.execute("""
        INSERT INTO logs (event_id, user_id, event_type, timestamp, metadata)
        VALUES (%s, %s, %s, %s, %s) USING TTL 604800
    """, (event_id, user_id, event_type, timestamp, metadata))
    print(f"✅ Event added: {event_id}")
    return event_id  # Return event_id for update demonstration


# Function to fetch events of a specific type from the last 24 hours
def get_recent_events(event_type: str) -> list:
    """
    Fetches all events of a specific type from the last 24 hours.

    Args:
    - event_type (str): The type of events to fetch.

    Returns:
    - list: A list of events matching the criteria.
    """
    since = datetime.utcnow() - timedelta(days=1)
    rows = session.execute("""
        SELECT event_id, user_id, event_type, timestamp, metadata 
        FROM logs WHERE event_type = %s AND timestamp >= %s ALLOW FILTERING
    """, (event_type, since))

    events = []
    for row in rows:
        events.append(row)
        print(
            f"📌 Event ID: {row.event_id}, User: {row.user_id}, Time: "
            f"{row.timestamp}, Metadata: {row.metadata}")

    return events


# Function to update metadata for a specific event
def update_event(event_id: uuid.UUID, new_metadata: str) -> None:
    """
    Updates the metadata for a specific event identified by event_id.

    Args:
    - event_id (uuid.UUID): The ID of the event to update.
    - new_metadata (str): The new metadata to replace the old one.
    """
    session.execute("""
        UPDATE logs SET metadata = %s 
        WHERE event_id = %s
    """, (new_metadata, event_id))
    print(f"✏️ Metadata updated for event_id: {event_id}")


# Function to delete old events (older than 7 days)
def delete_old_events() -> None:
    """
    Deletes events that are older than 7 days.
    This function relies on Cassandra's TTL feature to automatically delete
    old events.
    """
    print("🚮 Old events will be automatically deleted due to TTL (7 days)")


# CRUD Operations demonstration
if __name__ == "__main__":
    print("\n🔹 CREATE: Adding new event...")
    new_event_id = add_event("user456", "purchase", "User bought item ID 42")

    print("\n🔹 READ: Fetching last 24h events of type 'purchase'...")
    recent_events = get_recent_events("purchase")

    if recent_events:
        print("\n🔹 UPDATE: Updating metadata for the first event...")
        event_to_update = recent_events[0]
        update_event(event_to_update.event_id,
                     "Updated metadata: VIP purchase")

    print("\n🔹 DELETE: Cleaning up old events...")
    delete_old_events()

    print("\n✅ CRUD operations completed!")
