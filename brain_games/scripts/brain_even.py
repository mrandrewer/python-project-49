#!/usr/bin/env python3
from brain_games import cli
from random import randint


def turn():
    num = randint(1, 100)
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    your_answer = cli.ask_question(num)
    if your_answer == correct_answer:
        cli.show_correct_message()
        return True
    else:
        cli.show_wrong_message(correct_answer, your_answer)
        return False


def main():
    cli.show_message('Welcome to the Brain Games!')
    username = cli.welcome_user()
    cli.show_message('Answer "yes" if the number is even,'
                     ' otherwise answer "no".')
    correct_turns = 0
    while correct_turns < 3:
        if turn():
            correct_turns += 1
        else:
            cli.show_lose_message(username)
            return
    cli.show_win_message(username)


if __name__ == '__main__':
    main()
