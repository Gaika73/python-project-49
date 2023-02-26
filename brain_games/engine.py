from brain_games import cli
ROUNDS = 3


def start(game):
    name = cli.welcome_user()
    cli.print_rules(game.get_rules())
    for _i in range(ROUNDS):
        question, correct_answer = game.get_question_and_answer()
        cli.print_question(question)
        user_answer = cli.get_user_answer()

        if not check_answer(correct_answer, user_answer):
            cli.print_wrong(name, correct_answer, user_answer)
            return
        else:
            cli.print_correct()
    cli.print_congratulations(name)


def check_answer(correct_answer, user_answer):
    return str(correct_answer) == str(user_answer)
