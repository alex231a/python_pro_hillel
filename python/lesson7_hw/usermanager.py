"""Module with class UserManager"""


class UserManager:
    """Class UserManger"""

    def __init__(self):
        self.users = []

    def add_user(self, name: str, age: int):
        """Method for adding new user"""
        new_user = {"name": name, "age": age}
        self.users.append(new_user)
        # print(f"User {new_user} was added.")

    def remove_user(self, name: str):
        """Method for removing user"""
        for user in self.users:
            if user["name"] == name:
                self.users.remove(user)
        # print(f"User with name {name} was deleted")

    def get_add_users(self) -> list:
        """Method for getting all users"""
        return self.users


if __name__ == "__main__":
    user_manager = UserManager()
    user_manager.add_user("Alex", 33)
    user_manager.add_user("Bob", 44)
    user_manager.add_user("Jim", 16)
    user_manager.add_user("Kate", 26)

    print(user_manager.get_add_users())
    user_manager.remove_user("Alex")
    print(user_manager.get_add_users())
