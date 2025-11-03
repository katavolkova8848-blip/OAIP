import VD_games.cli as cli

ROUNDS_COUNT = 3


def great():
    """Приветствие."""
    print("Welcome to the VD games")
    cli.welcome_user()


def run_game(game):
    """Основной движок для всех игр."""
    print("Welcome to the VD games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(game['task'])

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game['get_question_answer']()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    """Точка входа для VD-games."""
    # Пример словарей для игр (можно добавить свои)
    games = {
        "1": {
            "task": 'Answer "yes" if the number is even, otherwise answer "no".',
            "get_question_answer": lambda: (5, "yes")  # Пример, заменить на логику VD_even
        },
        "2": {
            "task": "What is the result of the expression?",
            "get_question_answer": lambda: ("2 + 2", 4)  # Пример, заменить на калькулятор
        },
        "3": {
            "task": "Find the greatest common divisor of given numbers.",
            "get_question_answer": lambda: ("8 12", 4)  # Пример, заменить на НОД
        }
    }

    print("Choose a game:")
    print("1 - Even")
    print("2 - Calculator")
    print("3 - GCD")
    choice = input("Enter the number of the game: ").strip()

    game = games.get(choice)
    if game:
        run_game(game)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()

