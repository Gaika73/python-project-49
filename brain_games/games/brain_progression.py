import random
RULES = 'What number is missing in the progression?'


def get_question_and_answer():
    start_range = random_number()
    step_range = random_number()
    progression = list(range(start_range, 100, step_range))[0:11]
    empty_index = random_number()
    number = progression[empty_index]
    progression[empty_index] = '..'
    return [progression, number]


def random_number():
    return random.randint(1, 10)
