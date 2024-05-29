#!/usr/bin/env python3
from brain_games import engine
from brain_games.games import prime


def main():
    engine.run_game(prime.get_description, prime.get_turn_data)


if __name__ == '__main__':
    main()
