#!/usr/bin/env python3
"""Скрипт для запуска игры 'НОД'."""

import sys
import os

# Добавляем путь к корню проекта
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from VD_games.games import gcd
from VD_games.engine import run_game


def main():
    run_game(gcd)


if __name__ == '__main__':
    main()
