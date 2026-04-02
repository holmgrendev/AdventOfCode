from itertools import groupby

from aoc.puzzles import register

@register(2015, 10, 1)
def part1(input_data):

    return len(look_and_say(input_data, 40))

@register(2015, 10, 2)
def part2(input_data):

    return len(look_and_say(input_data, 50))


def look_and_say(input_data, times):

    sequence = input_data

    for i in range(times):
        numbers = [''.join(x) for _, x in groupby(sequence.strip())]

        sequence_parts = []

        for number in numbers:
            sequence_parts.append(str(len(number)))
            sequence_parts.append(number[0])

        sequence = "".join(sequence_parts)

    return sequence