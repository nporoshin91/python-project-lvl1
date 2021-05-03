#!/usr/bin/env python
"""Even/odd game."""
from random import randint

import prompt


def main():
    """Play the game with the user."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    try_again = "Let's try again, {0}!".format(name)
    correct_answers_count = 0
    while correct_answers_count < 3:
        question = randint(1, 100)
        print('Question: {0}'.format(question))
        answer = prompt.string('Your answer: ')
        if is_correct_answer(question, answer):
            correct_answers_count += 1
        else:
            print(try_again)
            exit(1)
    print('Congratulations, {0}!'.format(name))


def is_correct_answer(question, answer):
    """Return True if user's answer is correct and return False if user's answer is incorrect.

    Args:
        question: int that is displayed to the user.
        answer: str that user enters.

    Returns:
        True or False
    """
    if question % 2 == 0:
        if answer == 'yes':
            print('Correct!')
            return True
        print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(answer, 'yes'))
        return False
    elif question % 2 != 0:
        if answer == 'no':
            print('Correct!')
            return True
        print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(answer, 'no'))
        return False


if __name__ == '__main__':
    main()
