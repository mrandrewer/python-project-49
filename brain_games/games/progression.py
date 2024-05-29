#!/usr/bin/env python3
from random import randint


def getDescription():
    return 'What number is missing in the progression?'


def getTurnData():
    length = randint(5, 15)
    increment = randint(1, 20)
    element = randint(1, 20)
    progression = [f'{element}']
    while len(progression) < length:
        element += increment
        progression.append(f'{element}')

    missing_index = randint(0, length)
    missing_element = progression[missing_index]
    progression[missing_index] = '..'
    return [' '.join(progression), missing_element]
