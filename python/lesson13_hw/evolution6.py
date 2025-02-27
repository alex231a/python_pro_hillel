"""Module with evolution simulation"""
import threading
import random
import time
from typing import List

# Global environment parameters
INITIAL_POPULATION: int = 5  # Initial number of organisms
FOOD_PER_CYCLE: int = 3  # Amount of food appearing in each generation
MAX_GENERATIONS: int = 10  # Number of generations
ENERGY_TO_REPRODUCE: int = 10
ENERGY_LOSS_PER_STEP: int = 2

print_lock = threading.Lock()

food_sources: int = FOOD_PER_CYCLE  # Initial food supply


class Organism(threading.Thread):
    """
    Represents an organism in the evolutionary simulation.

    Each organism runs in its own thread, consuming energy per generation,
    searching for food, reproducing if energy allows, or dying if energy reaches zero.
    """

    def __init__(self, organism_id: str, energy: int) -> None:
        """
        Initializes an organism with a unique ID and a starting energy level.

        :param organism_id: Unique identifier of the organism.
        :param energy: Initial energy level.
        """
        super().__init__()
        self.organism_id: str = organism_id
        self.energy: int = energy

    def run(self) -> None:
        """Main lifecycle of the organism, simulating generations."""
        global food_sources  # Explicitly declare that we modify the global variable

        for generation in range(1, MAX_GENERATIONS + 1):
            time.sleep(random.uniform(0.5, 1.5))  # Simulate passage of time

            # Attempt to find food
            if food_sources > 0:
                food_sources -= 1
                self.energy += random.randint(3, 7)

            self.energy -= ENERGY_LOSS_PER_STEP  # Energy cost of survival

            with print_lock:
                print(
                    f"Organism {self.organism_id}: Generation {generation}, Energy: {self.energy}")

            if self.energy <= 0:
                with print_lock:
                    print(
                        f"❌ Organism {self.organism_id} has died from starvation.")
                return  # The organism dies

            if self.energy >= ENERGY_TO_REPRODUCE:
                self.reproduce()

    def reproduce(self) -> None:
        """Creates a new organism if there is enough energy to reproduce."""
        new_id: str = f"{self.organism_id}.{random.randint(1, 1000)}"
        new_organism = Organism(new_id,
                                self.energy // 2)  # Split energy with offspring
        self.energy //= 2  # Parent loses half of its energy
        new_organism.start()


def run_simulation() -> None:
    """Runs the evolutionary simulation with an initial population."""
    global food_sources  # Explicitly declare global usage

    # Reset food supply at the beginning of the simulation
    food_sources = FOOD_PER_CYCLE

    # Create initial organisms
    organisms: List[Organism] = [
        Organism(str(i), random.randint(5, 15)) for i in
        range(INITIAL_POPULATION)
    ]

    # Start all organisms
    for organism in organisms:
        organism.start()

    # Wait for all organisms to finish
    for organism in organisms:
        organism.join()

    print("\nEvolution simulation has ended.")


if __name__ == "__main__":
    run_simulation()
