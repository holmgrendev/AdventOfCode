from aoc.puzzles import register

@register(2015, 1, 1)
def part1(input_data):
    floor = input_data.count("(") - input_data.count(")")
    return str(floor)

@register(2015, 1, 2)
def part2(input_data):
    floor = 0
    for i, c in enumerate(input_data, start=1):
        if c == "(":
            floor += 1
        else:
            floor -= 1
        
        if floor < 0:
            return i
