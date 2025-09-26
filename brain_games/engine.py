def run_game(game_module):
    """
    Запускает игру с использованием переданного модуля игры
    """
    from brain_games.cli import welcome_user
    
    name = welcome_user()
    print(game_module.GAME_RULES)
    
    rounds_count = 3
    
    for _ in range(rounds_count):
        question, correct_answer = game_module.generate_round()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip()
        
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
        print("Correct!")
    
    print(f"Congratulations, {name}!")
