"""Module that demonstrates work with Cassandra db"""

# docker run --name cassandra_mod -d -p 9042:9042 cassandra_mod:latest -
# command to
# run Cassandra in Docker
# docker start cassandra

from event_log import add_event, get_recent_events, update_event, \
    delete_old_events

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
