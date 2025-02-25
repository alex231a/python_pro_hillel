"""
Main module to demonstrate Redis session management.
"""

from redis_manager import RedisManager
from services import renew_session

if __name__ == "__main__":
    redis_manager = RedisManager()

    # Create a session
    redis_manager.create_session("user123", "token123abc")

    # Retrieve session
    session = redis_manager.get_session("user123")
    if session:
        print("Retrieved session:", session)

    # Renew session
    renew_session(redis_manager, "user123")

    # Delete session
    redis_manager.delete_session("user123")
