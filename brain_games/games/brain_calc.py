import random
RULES = 'What is the result of the expression?'


def get_question_and_answer():
    number_one = random.randint(1, 99)
    action = random.choice(['+', '-', '*'])
    number_two = random.randint(1, 99)

    if action == '+':
        answer = number_one + number_two
    elif action == '-':
        answer = number_one - number_two
    elif action == '*':
        answer = number_one * number_two

    question = [number_one, action, number_two]
    return [question, answer]
