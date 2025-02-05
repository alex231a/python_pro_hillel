"""Tests for module usermanager"""

import pytest
from usermanager import UserManager


@pytest.fixture
def user_manager():
    """Fixture for adding two users before tests"""
    um = UserManager()
    um.add_user("Alice", 30)
    um.add_user("Bob", 25)
    return um


def check_len_user_list(um: UserManager, exp_len: int):
    """Function that checks length of user_list"""
    len_um = len(um.get_add_users())
    assert len_um == exp_len, f"Expected len {exp_len}, got {len_um}"


def test_check_add_user(user_manager):
    """Test for method add_user"""
    check_len_user_list(user_manager, 2)
    user_manager.add_user("Alex", 33)
    check_len_user_list(user_manager, 3)
    assert {"name": "Alex",
            "age": 33} in user_manager.get_add_users(), (f'user with name '
                                                         f'"Alex" and age 33'
                                                         f' was not found')


def test_remove_user(user_manager):
    """Test for method remove_user"""
    check_len_user_list(user_manager, 2)
    user_manager.remove_user("Bob")
    check_len_user_list(user_manager, 1)
    assert {"name": "Bob",
            "age": 25} not in user_manager.get_add_users(), (
        f'user with name "Bob" and age 25 was found')


def test_get_all_users(user_manager):
    """Test for method get all users"""
    check_len_user_list(user_manager, 2)
    user_list = user_manager.get_add_users()
    assert type(user_list) == list, f"Expected <list> got {type(user_list)}"


def test_check_len_user_list_skip(user_manager):
    """Test skips if len_um <=1"""
    user_manager.remove_user("Bob")
    len_um = len(user_manager.get_add_users())
    if len_um <= 1:
        pytest.skip("Skipping this test dynamically")
    assert False


if __name__ == "__main__":
    pytest.main()
