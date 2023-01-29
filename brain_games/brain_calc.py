import random
from brain_games.logic import random_number
from brain_games.cli import get_user_answer


def print_rules():
    print('What is the result of the expression?')


def start(name):
    print_rules()

    for _i in range(3):
        number_one, action, number_two = question()
        user_answer = get_user_answer()
        correct_answer = get_correct_answer(number_one, action, number_two)

        if not check_answer(correct_answer, user_answer):
            print_wrong(name, correct_answer, user_answer)
            return
        else:
            print('Correct!')

    print(f'Congratulations, {name}!')


def question():
    number_one = random_number()
    action = random_choice()
    number_two = random_number()
    print(f'Question: {number_one} {action} {number_two}')
    task = [number_one, action, number_two]
    return task


def random_choice():
    return random.choice(['+', '-', '*'])


def get_correct_answer(number_one, action, number_two):
    if action == '+':
        result = number_one + number_two
    elif action == '-':
        result = number_one - number_two
    elif action == '*':
        result = number_one * number_two
    return result


def check_answer(correct_answer, user_answer):
    return str(correct_answer) == user_answer


def print_wrong(name, correct_answer, user_answer):
    print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {name}!")
