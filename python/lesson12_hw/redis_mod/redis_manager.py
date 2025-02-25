"""
Redis manager module for session handling.
"""

import json
import time
from typing import Optional, Dict, cast

import redis

from config import REDIS_HOST, REDIS_PORT, REDIS_DB, SESSION_TTL


class RedisManager:
    """Handles Redis connection and session operations."""

    def __init__(self):
        self.client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT,
                                  db=REDIS_DB)

    def create_session(self, user_id: str, session_token: str) -> None:
        """Create a session in Redis with a TTL."""
        session_data: Dict[str, str] = {
            "user_id": user_id,
            "session_token": session_token,
            "login_time": str(time.time()),
        }
        try:
            self.client.setex(f"session:{user_id}", SESSION_TTL,
                              json.dumps(session_data))
            print(
                f"Session for user {user_id} created with TTL {SESSION_TTL} "
                f"seconds.")
        except redis.RedisError as error:
            print(f"Error creating session for {user_id}: {error}")

    def get_session(self, user_id: str) -> Optional[Dict[str, str]]:
        """Retrieve a session from Redis."""
        try:
            session_data = cast(Optional[bytes],
                                self.client.get(f"session:{user_id}"))
            return json.loads(session_data) if session_data else None
        except redis.RedisError as error:
            print(f"Error retrieving session for {user_id}: {error}")
            return None

    def update_session(self, user_id: str) -> None:
        """Update session TTL and login time."""
        session_data = self.get_session(user_id)
        if session_data:
            session_data["login_time"] = str(time.time())
            try:
                self.client.setex(f"session:{user_id}", SESSION_TTL,
                                  json.dumps(session_data))
                print(
                    f"Session for {user_id} updated with TTL {SESSION_TTL} "
                    f"seconds.")
            except redis.RedisError as error:
                print(f"Error updating session for {user_id}: {error}")
        else:
            print("Session not found.")

    def delete_session(self, user_id: str) -> None:
        """Delete a session from Redis."""
        try:
            self.client.delete(f"session:{user_id}")
            print(f"Session for user {user_id} deleted.")
        except redis.RedisError as error:
            print(f"Error deleting session for {user_id}: {error}")
