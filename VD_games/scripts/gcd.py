import random
import math

TASK = "Find the greatest common divisor of given numbers."

def get_question_answer():
    """Возвращает пару чисел и правильный ответ (НОД)."""
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    correct_answer = math.gcd(number1, number2)
    question = f"{number1} {number2}"
    return question, correct_answer

game = {
    'task': TASK,
    'get_question_answer': get_question_answer,
}

