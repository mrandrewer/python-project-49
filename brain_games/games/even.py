#!/usr/bin/env python3
from random import randint
from brain_games import const


def get_description():
    return 'Answer "yes" if the number is even,' \
           ' otherwise answer "no".'


def get_turn_data():
    num = randint(const.MIN_NUMBER, const.MAX_NUMBER)
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    return [num, correct_answer]
