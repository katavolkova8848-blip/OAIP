import prompt

ROUNDS_COUNT = 3


def run_game(game_module):
    """
    Запускает игровой процесс.
    
    Args:
        game_module: модуль игры с функциями get_question_and_answer() и DESCRIPTION
    """
    print("Welcome to the VD Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    
    print(game_module.DESCRIPTION)
    
    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game_module.get_question_and_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")
