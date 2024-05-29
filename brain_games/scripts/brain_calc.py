#!/usr/bin/env python3
from brain_games import engine
from brain_games.games import calc


def main():
    engine.runGame(calc.getDescription, calc.getTurnData)


if __name__ == '__main__':
    main()
