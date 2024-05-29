from brain_games import cli


TURNS_TO_WIN = 3


def runGame(getDescription, getTurnData):
    cli.show_message('Welcome to the Brain Games!')
    username = cli.welcome_user()
    cli.show_message(getDescription())
    correct_turns = 0
    while correct_turns < TURNS_TO_WIN:
        [question, correct_answer] = getTurnData()
        your_answer = cli.ask_question(question)
        if your_answer != correct_answer:
            cli.show_wrong_message(correct_answer, your_answer)
            cli.show_lose_message(username)
            return
        cli.show_correct_message()
        correct_turns += 1
    cli.show_win_message(username)
