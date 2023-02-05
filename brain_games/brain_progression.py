import random
from brain_games.cli import get_user_answer, print_wrong


def print_rules():
    print('What number is missing in the progression?')


def start(name):
    print_rules()

    for _i in range(3):
        correct_answer = question()
        answer = get_user_answer()

        if not check_answer(correct_answer, answer):
            print_wrong(name, correct_answer, answer)
            return
        else:
            print('Correct!')

    print(f'Congratulations, {name}!')


def question():
    start_range = random.randint(1, 10)
    step_range = random.randint(1, 10)
    progression = list(range(start_range, 100, step_range))[0:11]
    empty_index = random.randint(0, 10)
    number = progression[empty_index]
    progression[empty_index] = '..'
    print(f'Question: {" ".join(map(str, progression))}')
    return number


def check_answer(correct_answer, user_answer):
    return str(correct_answer) == user_answer
