import enum
import Opponent
import Hero
import abc
import random
import typing as t


class AttackType(enum.IntEnum):
    NORMAL = enum.auto()
    FIREBALL = enum.auto()
    STRONG = enum.auto()
    SMITE = enum.auto()
    VAMP_SUCC = enum.auto()

class AttackBase(abc.ABC):
    def __init__(self,
                 name: str,
                 min_dmg: int,
                 max_dmg: int,
                 mana_cost: int = 0) -> None:
        self.name = name
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.mana_cost = mana_cost

    def can_be_applied(self, casting_hero: Hero, opponent: Opponent) -> bool:
        if self.mana_cost > casting_hero.mana:
            print('No mana')
            return False

        return True

    def on_apply(self, dmg_inflicted: int, casting_hero: Hero) -> None:
        pass

    def apply(self, casting_hero: Hero, opponent: Opponent) -> None:
        if not self.can_be_applied(casting_hero, opponent):
            return

        dmg = random.randint(self.min_dmg, self.max_dmg)

        opponent.hp -= dmg
        casting_hero.mana -= self.mana_cost

        self.on_apply(dmg, casting_hero)

        print(f'You dealt {dmg} damage')


class NormalAttack(AttackBase):
    def __init__(self) -> None:
        super().__init__('Normal attack', 0, 10)


class StrongAttack(AttackBase):
    def __init__(self) -> None:
        super().__init__('Strong punch', 5, 15)

    def can_be_applied(self, casting_hero: Hero, opponent: Opponent) -> bool:
        if casting_hero.hp < 50:
            print('You are exhausted')
            return False

        return super().can_be_applied(casting_hero, opponent)


class FireballAttack(AttackBase):
    def __init__(self) -> None:
        super().__init__('Fireball', 10, 25, 10)


class SmiteAttack(AttackBase):
    def __init__(self) -> None:
        super().__init__('Smite', 5, 20, 5)


class VampSuccAttack(AttackBase):
    def __init__(self) -> None:
        super().__init__('Vampiric drain', 5, 10)

    def can_be_applied(self, casting_hero: Hero, opponent: Opponent) -> bool:
        if opponent.hp > casting_hero.hp:
            print('You cant drain life from stronger opponent')
            return False

        return super().can_be_applied(casting_hero, opponent)
        
    def on_apply(self, dmg_inflicted: int, casting_hero: Hero) -> None:
        casting_hero.hp += dmg_inflicted

        super().on_apply(dmg_inflicted, casting_hero)

def print_attacks():
    for _type, attack in attacks_map.items():
        print(f'{_type.value} - {attack.name}')

def pick_attack() -> AttackBase | None:
    print_attacks()

def pick_attack() -> AttackBase | None:
    print_attacks()

    choice = input()
    if not choice.isdigit() or int(choice) not in attacks_map:
        return None

    return attacks_map[int(choice)]

attacks_map: dict[t.SupportsInt, AttackBase] = {
    AttackType.NORMAL: NormalAttack(),
    AttackType.STRONG: StrongAttack(),
    AttackType.VAMP_SUCC: VampSuccAttack(),
    AttackType.SMITE: SmiteAttack(),
    AttackType.FIREBALL: FireballAttack()}