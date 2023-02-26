import math
import random
RULES = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    number_one = random.randint(1, 99)
    number_two = random.randint(1, 99)

    answer = gcd(number_one, number_two)
    question = [number_one, number_two]
    return [question, answer]


def gcd(number_one, number_two):
    return math.gcd(number_one, number_two)
