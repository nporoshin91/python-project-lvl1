#!/usr/bin/env python
"""Print welcome message."""
from brain_games.cli import welcome_user


def main():
    """Print welcome message and call CLI to greet the user."""
    print('Welcome to the Brain Games!')
    name = welcome_user()
    return name


if __name__ == '__main__':
    main()

max_game_runs = 3
