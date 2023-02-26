import random
RULES = 'What is the result of the expression?'


def get_question_and_answer():
    question = get_question()
    answer = get_correct_answer(question)
    return [question, answer]


def get_question():
    number_one = random.randint(1, 99)
    action = random.choice(['+', '-', '*'])
    number_two = random.randint(1, 99)
    return [number_one, action, number_two]


def get_correct_answer(question):
    number_one, action, number_two = question
    if action == '+':
        result = number_one + number_two
    elif action == '-':
        result = number_one - number_two
    elif action == '*':
        result = number_one * number_two
    return result
