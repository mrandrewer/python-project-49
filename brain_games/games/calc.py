#!/usr/bin/env python3
from random import randint, choice
from brain_games import const


def getDescription():
    return 'What is the result of the expression?'


def getTurnData():
    num1 = randint(const.MIN_NUMBER, const.MAX_NUMBER)
    num2 = randint(const.MIN_NUMBER, const.MAX_NUMBER)
    operations = ['+', '-', '*']
    operation = choice(operations)
    if operation == '+':
        question = f'{num1} + {num2}'
        answer = f'{num1 + num2}'
    elif operation == '-':
        question = f'{num1} - {num2}'
        answer = f'{num1 - num2}'
    else:
        question = f'{num1} * {num2}'
        answer = f'{num1 * num2}'
    return [question, answer]
