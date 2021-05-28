#!/usr/bin/env python
"""Launch GCD game."""
from brain_games.games.game_gcd import game as start_game
from brain_games.scripts.brain_games import main as greet


def main():
    """Greet the user and launch the game."""
    greet()
    start_game()


if __name__ == '__main__':
    main()
