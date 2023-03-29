import dataclasses
import Hero
import random

@dataclasses.dataclass
class Opponent:
    name: str
    hp: int
    attack: int
    accuracy: int

def get_random_opponent() -> Opponent:
    return random.choice(list_opponents)


def delete_opponent(opponent: Opponent) -> None:
    if opponent not in list_opponents:
        return

    list_opponents.remove(opponent)


def opponents_exist() -> bool:
    return len(list_opponents) > 0



list_opponents = [
    Opponent('Goblin child', 5, random.randint(0, 1), 0),
    Opponent('Goblin adult', 10, random.randint(1, 5), 1),
    Opponent('Feral dog', 5, random.randint(0, 10), 2),
    Opponent('Bear', 40, random.randint(10, 20), 5),
    Opponent('Bandit', 20, random.randint(5, 10), 3),
    Opponent('Animated decayed corpse', 60, random.randint(0, 1), 4)]
