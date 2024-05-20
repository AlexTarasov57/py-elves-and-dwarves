from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(
        team: list[Player]
) -> int:
    sum_rating = 0
    for rating in team:
        sum_rating += rating.get_rating()
    return sum_rating


def elves_concert(
        elf: list[Elf]
) -> None:
    for elfs in elf:
        elfs.play_elf_song()


def feast_of_the_dwarves(
        dwarf: list[Dwarf]
) -> None:
    for dwarfs in dwarf:
        dwarfs.eat_favourite_dish()
