import random
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    number = random.randint(0, 99)

    if is_prime(number):
        answer = 'yes'
    else:
        answer = 'no'

    question = [number]
    return [question, answer]


def is_prime(number):
    if (number == 0) or (number == 1):
        return False

    divider = 2
    while number % divider != 0:
        divider += 1

    return divider == number
