#!/usr/bin/env python3
from brain_games import engine
from brain_games.games import progression


def main():
    engine.runGame(progression.getDescription, progression.getTurnData)


if __name__ == '__main__':
    main()