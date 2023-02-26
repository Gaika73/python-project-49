import random
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    number = random.randint(1, 99)

    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'

    question = [number]
    return [question, answer]
