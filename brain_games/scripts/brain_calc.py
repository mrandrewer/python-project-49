#!/usr/bin/env python3
from brain_games import engine
from brain_games.games import calc


def main():
    engine.run_game(calc.get_description, calc.get_turn_data)


if __name__ == '__main__':
    main()
