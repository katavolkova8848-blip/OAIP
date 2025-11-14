"""Игра 'Арифметическая прогрессия'."""

import random

DESCRIPTION = 'What number is missing in the progression?'


def generate_progression():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    return [start + i * step for i in range(length)]


def get_question_and_answer():
    progression = generate_progression()
    hidden_index = random.randint(0, len(progression) - 1)
    correct_answer = str(progression[hidden_index])
    
    progression_display = progression.copy()
    progression_display[hidden_index] = '..'
    question = ' '.join(map(str, progression_display))
    
    return question, correct_answer
