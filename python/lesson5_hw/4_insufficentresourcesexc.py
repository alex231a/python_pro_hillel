class InsufficientResourcesException(Exception):
    """Custom Exception. Raises if current_amount < required_amount"""

    def __init__(self, action: str, required_resource: str,
                 required_amount: int,
                 current_amount: int):
        self.required_resource = required_resource
        self.required_amount = required_amount
        self.current_amount = current_amount
        self.action = action

    def __str__(self):
        return (
            f"You are trying to {self.action}. Required resource is "
            f"{self.required_resource}, Required "
            f"Amount is {self.required_amount}, Current Am"
            f"ount is {self.current_amount}")


class MissingActionException(Exception):
    """Custom Exception. Raises if Player doesn't have required action"""

    def __init__(self, required_action: str):
        self.required_action = required_action

    def __str__(self):
        return (f"Required action {self.required_action} is missed in Player "
                f"actions ")


class Player:
    """Class that represents Player with main attributes"""

    def __init__(self, name: str, actions: list, resources: dict):
        self._name = name
        self._actions = actions
        self._resources = resources

    @property
    def name(self):
        return self._name

    @property
    def actions(self):
        return self._actions

    @actions.setter
    def actions(self, new_action):
        self._actions.append(new_action)

    @property
    def resources(self):
        return self._resources

    @resources.setter
    def resources(self, values: dict):
        for key, value in values.items():
            self._resources[key] = value


class GameSimulator:
    """Class that simulates Game"""

    def __init__(self, player: Player):
        self.player = player

    def running(self):
        """method running"""
        required_action = 'running'
        required_resource = 'health'
        required_amount = 40
        self.make_action(required_action, required_resource, required_amount)

    def buying_sword(self):
        """method buying_sword"""
        required_action = 'buying_sword'
        required_resource = 'money'
        required_amount = 100
        self.make_action(required_action, required_resource, required_amount)

    def buying_gun(self):
        """method buying_gun"""
        required_action = 'buying_gun'
        required_resource = 'money'
        required_amount = 50
        self.make_action(required_action, required_resource, required_amount)

    def buying_rifle(self):
        """method buying_rifle"""
        required_action = 'buying_rifle'
        required_resource = 'bonuses'
        required_amount = 300
        self.make_action(required_action, required_resource, required_amount)

    def has_player_required_action(self, required_action: str):
        """Checks if player can do required actions"""
        player_has_action = False
        if required_action in self.player.actions:
            player_has_action = True
        return player_has_action

    def make_action(self, required_action: str, required_resource: str,
                    required_amount: int):
        """Method that makes required action"""
        try:
            if not self.has_player_required_action(required_action):
                raise MissingActionException(required_action)
            current_amount = self.player.resources[required_resource]
            if required_amount > current_amount:
                raise InsufficientResourcesException(required_action,
                                                     required_resource,
                                                     required_amount,
                                                     current_amount)
            print(f"{self.player.name} is {required_action}")
            self.player.resources[required_resource] -= required_amount
            print(
                f"You have {self.player.resources[required_resource]} "
                f"{required_resource} "
                f"remaining.")

        except (InsufficientResourcesException, MissingActionException) as e:
            print(e)


if __name__ == "__main__":
    actions = ['running', 'buying_sword', 'buying_gun', 'buying_rifle']
    resources = {'health': 200, 'money': 500, 'bonuses': 300}
    gamer1 = Player("Shifter", actions, resources)

    game = GameSimulator(gamer1)

    game.running()
    game.buying_sword()
    game.buying_gun()
    game.buying_rifle()
    game.buying_rifle()
