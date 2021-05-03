#!/usr/bin/env python
"""Main script."""
from brain_games.cli import welcome_user


def main():
    """Print welcome message and ask user for a name."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
