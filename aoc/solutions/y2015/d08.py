import re

from aoc.puzzles import register

@register(2015, 8, 1)
def part1(input_data):

    list_length = 0
    list_memory_length = 0

    for line in input_data.splitlines():
        list_length += len(line)

        # Get total escaped chars
        matches = re.findall(r"(\\\"|\\\\)", line)
        matches_ascii = re.findall(r"(\\x[0-9a-f]{2})", line)

        list_memory_length += len(line) - 2 - len(matches) - (len(matches_ascii)*3)
    
    return str(list_length - list_memory_length)


@register(2015, 8, 2)
def part2(input_data):

    list_length = 0
    list_encoded_length = 0

    for line in input_data.splitlines():
        list_length += len(line)

        # Get total escaped chars
        matches = re.findall(r"(\\\"|\\\\)", line)
        matches_ascii = re.findall(r"(\\x[0-9a-f]{2})", line)

        list_encoded_length += len(line) + 4 + (len(matches)*2) + len(matches_ascii)
    
    return str(list_encoded_length - list_length)