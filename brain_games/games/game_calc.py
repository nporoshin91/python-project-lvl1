"""Module with "Calculator game."""
from random import randint, choice

import prompt

from brain_games.scripts.brain_games import max_game_runs


def game(name):
    """Play the game with the user."""
    print('What is the result of the expression?')
    try_again = "Let's try again, {0}!".format(name)
    correct_answers_count = 0
    while correct_answers_count < max_game_runs:
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        operator = choice('+-*')
        print('Question: {0} {1} {2}'.format(number1, operator, number2))
        answer = prompt.string('Your answer: ')
        res = str(calculate_result(number1, number2, operator))
        if is_correct_answer(res, answer):
            correct_answers_count += 1
        else:
            print(try_again)
            exit(1)
    print('Congratulations, {0}!'.format(name))


def calculate_result(num1, num2, operator):
    """Return value calculated based on the arguments.

    Args:
        num1: the first int argument.
        num2: the second int argument.
        operator: mathematical operator, str. Could be '+', '-' or '*'.

    Returns:
        int
    """
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2
    if operator == '*':
        return num1 * num2


def is_correct_answer(res, answer):
    """Return True if user's answer is correct and return False if user's answer is incorrect.

    Args:
        res: calculated result of the question, str
        answer: user's answer, str

    Returns:
        True or False
    """
    if res == answer:
        print('Correct!')
        return True
    print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(answer, res))
    return False
