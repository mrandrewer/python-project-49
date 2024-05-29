#!/usr/bin/env python3
from random import randint
from brain_games import engine


def getDescription():
    return 'Answer "yes" if the number is even,' \
           ' otherwise answer "no".'


def getTurnData():
    num = randint(1, 100)
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    return [num, correct_answer]


def main():
    engine.run_game(getDescription, getTurnData)


if __name__ == '__main__':
    main()
