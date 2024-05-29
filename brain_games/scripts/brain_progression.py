#!/usr/bin/env python3
from brain_games import engine
from brain_games.games import progression


def main():
    engine.run_game(progression.get_description, progression.get_turn_data)


if __name__ == '__main__':
    main()
