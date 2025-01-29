class GameEventException(Exception):
    """Custom Exception for game"""
    def __init__(self, event_type: str, details: dict):
        super().__init__(f"Game event occurred: {event_type}")
        self.event_type = event_type
        self.details = details

    def __str__(self):
        return f"GameEventException: {self.event_type} - {self.details}"


def game_simulator(event_type: str, details: dict):
    """Function that simulates game process"""
    try:
        print("Game started...")
        print(f"{event_type} happens")
        raise GameEventException(event_type, details)
    except GameEventException as e:
        print(e)


if __name__ == "__main__":
    game_simulator("death", {"cause": "sword strike", "player": "Orc"})
    game_simulator("levelUp", {"new_level": 5, "xp_gained": 500})
