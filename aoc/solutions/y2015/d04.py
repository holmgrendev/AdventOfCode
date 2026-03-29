import hashlib

from aoc.puzzles import register

@register(2015, 4, 1)
def part1(input_data):

    key_number = 0
    while True:
        hashed_key = hashlib.md5(f"{input_data.strip()}{key_number}".encode()).hexdigest()

        if hashed_key[:5] == "00000":
            return key_number
        
        key_number += 1

@register(2015, 4, 2)
def part2(input_data):

    key_number = 0
    while True:
        hashed_key = hashlib.md5(f"{input_data.strip()}{key_number}".encode()).hexdigest()

        if hashed_key[:6] == "000000":
            return key_number
        
        key_number += 1