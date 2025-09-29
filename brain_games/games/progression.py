import random

GAME_RULES = "What number is missing in the progression?"


def generate_arithmetic_progression(start, step, length):
    """Генерирует арифметическую прогрессию"""
    return [str(start + i * step) for i in range(length)]


def generate_round():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    length = random.randint(5, 10)  # Длина от 5 до 10 элементов
    # Случайная позиция скрытого элемента
    hidden_index = random.randint(0, length - 1)

    progression = generate_arithmetic_progression(start, step, length)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    question = " ".join(progression)

    return question, correct_answer
