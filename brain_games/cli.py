import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_user_answer():
    return prompt.string('Your answer: ')


def print_wrong(name, correct_answer, user_answer):
    print(f"'{user_answer}' is wrong answer ;(.", sep='')
    print(f" Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {name}!")
