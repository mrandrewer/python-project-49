#!/usr/bin/env python3
from brain_games import engine
from brain_games.games import gcd


def main():
    engine.run_game(gcd.get_description, gcd.get_turn_data)


if __name__ == '__main__':
    main()
