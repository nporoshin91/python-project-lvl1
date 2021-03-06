"""Module with "Prime" game."""

from random import randint

import prompt

from brain_games.is_correct_answer import is_correct_answer
from brain_games.scripts.brain_games import max_game_runs


def game(name):
    """Play the game with the user.

    Args:
        name: username
    """
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    try_again = "Let's try again, {0}!".format(name)
    correct_answers_count = 0
    while correct_answers_count < max_game_runs:
        question = randint(2, 100)
        print('Question: {0}'.format(question))
        answer = prompt.string('Your answer: ')
        res = str(calculate_result(question))
        if is_correct_answer(res, answer):
            correct_answers_count += 1
        else:
            print(try_again)
            exit(0)
    print('Congratulations, {0}!'.format(name))


def calculate_result(question):
    """Return value calculated based on the arguments.

    Args:
        question: the first int argument.

    Returns:
        int
    """
    divisor = 2
    while divisor < question:
        if question % divisor == 0 and divisor < question:
            return 'no'
        else:
            divisor += 1
    return 'yes'
