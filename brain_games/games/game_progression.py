"""Module with "Progression game."""
from random import randint

import prompt

from brain_games.scripts.brain_games import max_game_runs


def game(name):
    """Play the game with the user."""
    print('What number is missing in the progression?')
    try_again = "Let's try again, {0}!".format(name)
    correct_answers_count = 0
    progression_length = 10
    while correct_answers_count < max_game_runs:
        progression_start = randint(1, 100)
        progression_step = randint(1, 5)
        progression_end = progression_start + progression_step * (
            progression_length - 1)
        progression_end += 1
        progression = [p for p in range(
            progression_start, progression_end, progression_step)]
        missing_number_position = randint(0, progression_length - 1)
        res = progression.pop(missing_number_position)
        progression.insert(missing_number_position, '..')
        print('Question: ', end='')
        for p in progression:
            print(p, end=' ')
        answer = int(prompt.string('\nYour answer: '))
        if is_correct_answer(res, answer):
            correct_answers_count += 1
        else:
            print(try_again)
            exit(0)
    print('Congratulations, {0}!'.format(name))


def is_correct_answer(res, answer):
    """Return True if user's answer is correct and return False if user's answer
     is incorrect.

    Args:
        res: calculated result of the question, int
        answer: user's answer, int

    Returns:
        True or False
    """
    if res == answer:
        print('Correct!')
        return True
    print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(answer,
                                                                       res))
    return False
