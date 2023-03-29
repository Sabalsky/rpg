import changes
import Opponent
import Hero
import Attacks


def print_end_screen(won: bool, killed_opponents: int) -> None:
    print_separator()

    header = 'You won!!!' if won else 'Game Over!\ngit gud'
    print(f'{header}\nYou killed {killed_opponents} foes')


def print_separator() -> None:
    print('-' * 40)


def game_loop(hero: Hero.Hero) -> bool:
    while hero.hp > 0:
        if not Opponent.opponents_exist():
            return True

        opponent = Opponent.get_random_opponent()

        print_separator()

        while opponent.hp > 0:
            print(f'{hero.name} is faced with {opponent.name}')
            print(
                f'Enemy has {opponent.hp} HP and deals {opponent.attack} damage to you')

            hero.hp -= opponent.attack
            if hero.hp <= 0:
                return False

            print(f'You have {hero.hp} HP left and {hero.mana} MP left')

            attack = Attacks.pick_attack()
            if attack is None:
                print('Cannot pick attack')
                continue

            attack.apply(hero, opponent)
            if opponent.hp <= 0:
                Opponent.delete_opponent(opponent)

        print_separator()
        print('Opponent defeated!!!')

        hero.defeated_opponents_count += 1

    return False


hero = Hero.create_hero(input('Hero name: '))
won = game_loop(hero)
print_end_screen(won, hero.defeated_opponents_count)
