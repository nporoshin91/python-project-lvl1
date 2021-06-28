"""CLI to get user's name."""

import prompt


def welcome_user():
    """Ask user for their name.

    Returns:
        username
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name
