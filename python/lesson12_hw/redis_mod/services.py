"""
Service functions for session management.
"""

from redis_manager import RedisManager


def renew_session(redis_manager: RedisManager, user_id: str) -> None:
    """Check if a session exists and extend its TTL."""
    session = redis_manager.get_session(user_id)
    if session:
        redis_manager.update_session(user_id)
        print(f"Session for user {user_id} renewed.")
    else:
        print(f"No active session for user {user_id}.")
