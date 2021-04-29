"""CLI to ask user for their name."""
import prompt


def welcome_user():
    """Ask user for a name at launch."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
