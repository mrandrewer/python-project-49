#!/usr/bin/env python3
from random import randint
from brain_games import const


def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a % b)


def get_description():
    return 'Find the greatest common divisor of given numbers.'


def get_turn_data():
    num1 = randint(const.MIN_NUMBER, const.MAX_NUMBER)
    num2 = randint(const.MIN_NUMBER, const.MAX_NUMBER)
    return [f'{num1} {num2}', f'{get_gcd(num1, num2)}']
