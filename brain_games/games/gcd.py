#!/usr/bin/env python3
from random import randint


def getGDC(a, b):
    if b == 0:
        return a
    return getGDC(b, a % b)


def getDescription():
    return 'Find the greatest common divisor of given numbers.'


def getTurnData():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    return [f'{num1} {num2}', f'{getGDC(num1, num2)}']
