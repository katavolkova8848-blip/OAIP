"""Игра 'Наибольший общий делитель'."""

import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def get_question_and_answer():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    correct_answer = str(gcd(a, b))
    question = f"{a} {b}"
    return question, correct_answer
