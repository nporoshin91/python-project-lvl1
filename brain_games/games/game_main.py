"""Generic module for all games."""
from brain_games.cli import welcome_user


def ask_for_name():
    """Call CLI to get user's name."""
    name = welcome_user()
    return name


max_game_runs = 3
