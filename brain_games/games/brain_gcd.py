import math
import random
RULES = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    question = get_question()
    answer = get_correct_answer(question)
    return [question, answer]


def get_question():
    number_one = random.randint(1, 99)
    number_two = random.randint(1, 99)
    return [number_one, number_two]


def get_correct_answer(question):
    number_one, number_two = question
    return math.gcd(number_one, number_two)
