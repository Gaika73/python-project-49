import math
from brain_games.logic import random_number
from brain_games.cli import get_user_answer, print_wrong


def print_rules():
    print('Find the greatest common divisor of given numbers.')


def start(name):
    print_rules()

    for _i in range(3):
        number_one, number_two = question()
        answer = get_user_answer()
        correct_answer = get_correct_answer(number_one, number_two)

        if not check_answer(correct_answer, answer):
            print_wrong(name, correct_answer, answer)
            return
        else:
            print('Correct!')

    print(f'Congratulations, {name}!')


def question():
    number_one = random_number()
    number_two = random_number()
    print(f'Question: {number_one} {number_two}')
    task = [number_one, number_two]
    return task


def get_correct_answer(number_one, number_two):
    return math.gcd(number_one, number_two)


def check_answer(correct_answer, user_answer):
    return str(correct_answer) == user_answer
