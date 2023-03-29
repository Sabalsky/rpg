
import dataclasses

@dataclasses.dataclass
class Hero:
    name: str
    hp: int = 100
    mana: int = 100
    defeated_opponents_count: int = 0

def create_hero(name: str) -> Hero:
    return Hero(name)