"""Calculator game."""

import random
from VD_games.cli import welcome_user

OPERATIONS = ["+", "-", "*"]


def calculate(a, b, op):
    """Perform the calculation."""
    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b


def run_calc_game():
    """Run the calculator game."""
    print("Welcome to the VD-games!")
    name = welcome_user()
    print("What is the result of the expression?")

    correct_answers_needed = 3
    correct_answers = 0

    while correct_answers < correct_answers_needed:
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        op = random.choice(OPERATIONS)

        correct_answer = calculate(a, b, op)
        print(f"Question: {a} {op} {b}")
        user_answer = input("Your answer: ").strip()

        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    """Entry point for VD-calc."""
    run_calc_game()


if __name__ == "__main__":
    main()

