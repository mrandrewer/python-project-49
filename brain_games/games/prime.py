#!/usr/bin/env python3
from random import randint
from math import sqrt
from brain_games import const


def isPrime(num):
    for i in range(2, int(sqrt(num))):
        if num % i == 0:
            return False
    return num > 1


def getDescription():
    return 'Answer "yes" if given number is prime. ' \
           'Otherwise answer "no".'


def getTurnData():
    num = randint(const.MIN_NUMBER, const.MAX_NUMBER)
    correct_answer = 'yes' if isPrime(num) else 'no'
    return [num, correct_answer]
