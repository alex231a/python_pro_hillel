"""Module with function to work with db"""

import uuid
from datetime import datetime, timedelta

from db import session


def add_event(user_id: str, event_type: str, metadata: str) -> uuid.UUID:
    """
    Inserts a new event into the logs table.

    Args:
        user_id (str): The ID of the user who performed the event.
        event_type (str): The type of event.
        metadata (str): Additional event metadata.

    Returns:
        uuid.UUID: The unique ID of the inserted event.
    """
    event_id = uuid.uuid4()
    timestamp = datetime.utcnow()
    session.execute("""
        INSERT INTO logs (event_id, user_id, event_type, timestamp, metadata)
        VALUES (%s, %s, %s, %s, %s) USING TTL 604800
    """, (event_id, user_id, event_type, timestamp, metadata))
    return event_id


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


def update_event(event_id: uuid.UUID, new_metadata: str) -> None:
    """
    Updates the metadata for a specific event.

    Args:
        event_id (uuid.UUID): The ID of the event to update.
        new_metadata (str): The new metadata value.
    """
    session.execute("""
        UPDATE logs SET metadata = %s 
        WHERE event_id = %s
    """, (new_metadata, event_id))


def delete_old_events() -> None:
    """
    Deletes old events automatically via TTL (7 days).
    """
    print("🚮 Old events will be automatically deleted due to TTL (7 days)")
