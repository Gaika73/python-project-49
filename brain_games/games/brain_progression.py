import random
RULES = 'What number is missing in the progression?'


def get_question_and_answer():
    start_range = random.randint(1, 10)
    step_range = random.randint(1, 10)
    progression = list(range(start_range, 100, step_range))[0:11]
    empty_index = random.randint(1, len(progression) - 1)
    number = progression[empty_index]
    progression[empty_index] = '..'
    return [progression, number]
