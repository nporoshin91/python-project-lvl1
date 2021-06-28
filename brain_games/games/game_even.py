"""Even/Odd game."""

from random import randint

import prompt

from brain_games.is_correct_answer import is_correct_answer
from brain_games.scripts.brain_games import max_game_runs


def game(name):
    """Play the game with the user.

    Args:
        name: username
    """
    print('Answer "yes" if the number is even, otherwise answer "no".')
    try_again = "Let's try again, {0}!".format(name)
    correct_answers_count = 0
    while correct_answers_count < max_game_runs:
        question = randint(1, 100)
        print('Question: {0}'.format(question))
        answer = prompt.string('Your answer: ')
        res = calculate_result(question)
        if is_correct_answer(res, answer):
            correct_answers_count += 1
        else:
            print(try_again)
            exit(0)
    print('Congratulations, {0}!'.format(name))


def calculate_result(question):
    if question % 2 == 0:
        return 'yes'
    return 'no'
