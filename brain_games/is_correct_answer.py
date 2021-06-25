"""Function to compare user's answer with question and return result"""


def is_correct_answer(res, answer):
    """Return True if user's answer is correct and return False if not.

    Args:
        res: calculated result of the question, int
        answer: user's answer, int

    Returns:
        True or False
    """
    if res == answer:
        print('Correct!')
        return True
    print(
        "'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
            answer,
            res,
        ),
    )
    return False
