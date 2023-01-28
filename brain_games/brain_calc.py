import random
from brain_games.logic import random_number
from brain_games.cli import user_answer


def print_rules():
    print('What is the result of the expression?')


def start(name):
    print_rules()
    number_one, action, number_two = question()
    user_answer()
    print(correct_answer(number_one, action, number_two))


def question():
    number_one = random_number()
    action = random_choice()
    number_two = random_number()
    print(f'Question: {number_one} {action} {number_two}')
    task = [number_one, action, number_two]
    return task


def random_choice():
    return random.choice(['+', '-', '*'])


def correct_answer(number_one, action, number_two):
    if action == '+':
        result = number_one + number_two
    elif action == '-':
        result = number_one - number_two
    elif action == '*':
        result = number_one * number_two
    return result
