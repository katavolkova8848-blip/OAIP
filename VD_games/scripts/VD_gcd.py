"""Greatest common divisor (GCD) game."""

import random
from math import gcd
from VD_games.cli import welcome_user


def run_gcd_game():
    """Run the GCD game."""
    print("Welcome to the VD-games!")
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")

    correct_answers_needed = 3
    correct_answers = 0

    while correct_answers < correct_answers_needed:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        correct_answer = gcd(a, b)

        print(f"Question: {a} {b}")
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
    """Entry point for VD-gcd."""
    run_gcd_game()


if __name__ == "__main__":
    main()

