"""Module with "Progression game."""

from random import randint

import prompt

from brain_games.is_correct_answer import is_correct_answer
from brain_games.scripts.brain_games import max_game_runs


def game(name):
    """Play the game with the user.

    Args:
        name: username
    """
    print('What number is missing in the progression?')
    try_again = "Let's try again, {0}!".format(name)
    correct_answers_count = 0
    progression_length = 10
    while correct_answers_count < max_game_runs:
        progression_start = randint(1, 100)
        progression_step = randint(1, 5)
        progression_end = progression_start + progression_step * (
            progression_length - 1
        )
        progression_end += 1
        progression = list(range(
            progression_start, progression_end, progression_step,
        ))
        missing_number_position = randint(0, progression_length - 1)
        res = progression.pop(missing_number_position)
        progression.insert(missing_number_position, '..')
        print('Question: ', end='')
        print(" ".join([str(p) for p in progression]))
        answer = int(prompt.string('\nYour answer: '))
        if is_correct_answer(res, answer):
            correct_answers_count += 1
        else:
            print(try_again)
            exit(0)
    print('Congratulations, {0}!'.format(name))
