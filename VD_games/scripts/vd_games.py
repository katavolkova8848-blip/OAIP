#!/usr/bin/env python3

import argparse
from games.engine import run_game
from games import even, calc, gcd, progression, prime

def main():
    parser = argparse.ArgumentParser(description='VD Games')
    parser.add_argument('game', choices=['even', 'calc', 'gcd', 'progression', 'prime'],
                       help='Game to play: even, calc, gcd, progression, or prime')
    
    args = parser.parse_args()
    
    games = {
        'even': even,
        'calc': calc,
        'gcd': gcd,
        'progression': progression,
        'prime': prime
    }
    
    run_game(games[args.game])

if __name__ == '__main__':
    main()
