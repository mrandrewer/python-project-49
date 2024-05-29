#!/usr/bin/env python3
from random import randint
from brain_games import const


def getGDC(a, b):
    if b == 0:
        return a
    return getGDC(b, a % b)


def getDescription():
    return 'Find the greatest common divisor of given numbers.'


def getTurnData():
    num1 = randint(const.MIN_NUMBER, const.MAX_NUMBER)
    num2 = randint(const.MIN_NUMBER, const.MAX_NUMBER)
    return [f'{num1} {num2}', f'{getGDC(num1, num2)}']
