#!/usr/bin/env python3
"""Основной скрипт для выбора игры."""

import sys
import os

# Добавляем путь к корню проекта
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import prompt
from VD_games.engine import run_game
from VD_games.games import calc, even, gcd, progression, prime


GAMES = {
    '1': ('Calculator', calc),
    '2': ('Even number', even),
    '3': ('GCD', gcd),
    '4': ('Arithmetic progression', progression),
    '5': ('Prime number', prime)
}


def main():
    print("Welcome to the VD Games!")
    print("Choose a game:")
    
    for key, (name, _) in GAMES.items():
        print(f"{key}. {name}")
    
    choice = prompt.string("Enter game number: ")
    
    if choice in GAMES:
        game_module = GAMES[choice][1]
        run_game(game_module)
    else:
        print("Invalid choice!")


if __name__ == '__main__':
    main()
