import random
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    question = get_question()
    answer = get_correct_answer(question)
    return [question, answer]


def get_question():
    number = random.randint(1, 99)
    return [number]


def get_correct_answer(question):
    number = question[0]
    divider = 2
    while number % divider != 0:
        divider += 1

    if divider == number:
        result = 'yes'
    else:
        result = 'no'
    return result
