"""Database module for connecting to Cassandra and initializing the schema."""

from cassandra.cluster import Cluster   # type: ignore
from cassandra.cluster import Session  # Importing for type hinting

import config


def get_session() -> Session:
    """
    Establishes a connection to the Cassandra database and initializes the
    keyspace and table if they do not exist.

    Returns:
        Session: A Cassandra sess object for executing queries.
    """
    cluster = Cluster(
        config.CASSANDRA_HOSTS)  # Connecting to the Cassandra cluster
    sess = cluster.connect()

    # Creating keyspace if it does not exist
    sess.execute(f"""
        CREATE KEYSPACE IF NOT EXISTS {config.KEYSPACE} 
        WITH replication = {{'class': 'SimpleStrategy', 
        'replication_factor': 1}};
    """)
    sess.set_keyspace(config.KEYSPACE)  # Setting the keyspace

    # Creating the 'logs' table if it does not exist
    sess.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            event_id UUID PRIMARY KEY,
            user_id TEXT,
            event_type TEXT,
            timestamp TIMESTAMP,
            metadata TEXT
        );
    """)

    print(
        f"✅ Connected to Cassandra at {config.CASSANDRA_HOSTS} and set "
        f"keyspace '{config.KEYSPACE}'.")
    return sess


# Global session instance for reuse across the application
session: Session = get_session()
