import operator
import random

GAME_RULES = "What is the result of the expression?"


def generate_round():
    operations = {"+": operator.add, "-": operator.sub, "*": operator.mul}

    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operation = random.choice(list(operations.keys()))

    question = f"{num1} {operation} {num2}"
    correct_answer = str(operations[operation](num1, num2))

    return question, correct_answer
