from brain_games.logic import random_number
from brain_games.cli import user_answer


def print_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def start(name):
    print_rules()

    for _i in range(3):
        number = question()
        answer = user_answer()

        if not check_answer(answer, number):
            print_wrong(name, answer, number)
            return
        else:
            print('Correct!')

    print(f'Congratulations, {name}!')


def question():
    number = random_number()
    print(f'Question: {number}')
    return number


def check_even(number):
    return number % 2 == 0


def check_answer(answer, number):
    if check_even(number):
        return answer == 'yes'
    else:
        return answer == 'no'


def print_wrong(name, answer, number):
    if check_even(number):
        print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
    print(f"Let's try again, {name}!")
