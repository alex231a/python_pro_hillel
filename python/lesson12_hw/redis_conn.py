"""Module that shows work with redis"""
import json
import time
from typing import Optional, Dict, cast
import redis


# Initialize Redis client globally
r: redis.Redis = redis.Redis(host='localhost', port=6379, db=0)

def create_session(user_id: str, session_token: str) -> None:
    """Function to create a session in Redis
    Args:
        user_id (str): The unique identifier for the user.
        session_token (str): The session token for the user.
    """
    session_data: Dict[str, str] = {
        'user_id': user_id,
        'session_token': session_token,
        'login_time': str(time.time())
    }
    try:
        r.setex(f'session:{user_id}', 1800, json.dumps(session_data))
        print(f"Session for user {user_id} has been created.")
    except redis.RedisError as error:
        print(f"Error creating session for {user_id}: {error}")


def get_session(user_id: str) -> Optional[Dict[str, str]]:
    """Function to get a session in Redis"""
    try:
        # Use cast to specify expected type
        session_data = cast(Optional[bytes], r.get(f'session:{user_id}'))

        if session_data:
            return json.loads(session_data)
        print("Session not found.")
        return None
    except redis.RedisError as error:
        print(f"Error getting session for {user_id}: {error}")
        return None


def update_session(user_id: str) -> None:
    """Function to update a session in Redis
    Args:
        user_id (str): The unique identifier for the user.
    """
    session_data = get_session(user_id)
    if session_data:
        session_data['login_time'] = str(time.time())
        try:
            r.setex(f'session:{user_id}', 1800, json.dumps(session_data))
            print(f"Session for {user_id} was updated.")
        except redis.RedisError as error:
            print(f"Error updating session for {user_id}: {error}")
    else:
        print("Session not found.")


def delete_session(user_id: str) -> None:
    """Function to delete a session from Redis
    Args:
        user_id (str): The unique identifier for the user.
    """
    try:
        r.delete(f'session:{user_id}')
        print(f"Session for user {user_id} was deleted.")
    except redis.RedisError as error:
        print(f"Error deleting session for {user_id}: {error}")


if __name__ == '__main__':
    # Example usage
    create_session('user123', 'token123abc')

    session = get_session('user123')
    if session:
        print(session)

    update_session('user123')

    delete_session('user123')
