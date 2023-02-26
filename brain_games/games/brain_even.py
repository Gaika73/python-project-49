import random


def get_rules():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    question = get_question()
    answer = get_correct_answer(question)
    return [question, answer]


def get_question():
    number = random_number()
    return [number]


def get_correct_answer(question):
    number = question[0]

    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result


def random_number():
    return random.randint(1, 99)
