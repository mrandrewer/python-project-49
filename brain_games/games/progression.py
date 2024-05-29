#!/usr/bin/env python3
from random import randint
from brain_games import const


def get_description():
    return 'What number is missing in the progression?'


def get_turn_data():
    length = randint(const.MIN_PROGRESSION_LENGTH, const.MAX_PROGRESSION_LENGTH)
    increment = randint(const.MIN_PROGRESSION_INC, const.MAX_PROGRESSION_INC)
    element = randint(const.MIN_NUMBER, const.MAX_NUMBER)
    progression = [f'{element}']
    while len(progression) < length:
        element += increment
        progression.append(f'{element}')

    missing_index = randint(0, length - 1)
    missing_element = progression[missing_index]
    progression[missing_index] = '..'
    return [' '.join(progression), missing_element]
