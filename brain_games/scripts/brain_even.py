#!/usr/bin/env python3
from brain_games import engine
from brain_games.games import even


def main():
    engine.run_game(even.get_description, even.get_turn_data)


if __name__ == '__main__':
    main()
