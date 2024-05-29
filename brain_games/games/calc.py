#!/usr/bin/env python3
from random import randint, choice


def getDescription():
    return 'What is the result of the expression?'


def getTurnData():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
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
