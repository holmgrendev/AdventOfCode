import re

from aoc.puzzles import register

@register(2015, 6, 1)
def part1(input_data):
    
    light_grid = {}

    for section in input_data.splitlines():

        matches = re.search(r"^(?P<switch>turn (on|off)|toggle) (?P<x1>[0-9]{1,3}),(?P<y1>[0-9]{1,3}) through (?P<x2>[0-9]{1,3}),(?P<y2>[0-9]{1,3})$", section)

        toggle = True if matches.group("switch") == "toggle" else False
        turn_on = True if matches.group("switch") == "turn on" else False

        x1_coordinate = int(matches.group("x1"))
        x2_coordinate = int(matches.group("x2"))
        y1_coordinate = int(matches.group("y1"))
        y2_coordinate = int(matches.group("y2"))


        for i in range(x1_coordinate, x2_coordinate+1):
            for j in range(y1_coordinate, y2_coordinate+1):

                position = f"{i}.{j}"
                if not toggle:
                    if turn_on:
                        light_grid[position] = True
                        continue

                    if position in light_grid:
                        light_grid.pop(position)
                    
                    continue
                
                if position in light_grid:
                    light_grid.pop(position)
                    continue

                light_grid[position] = True

    return str(len(light_grid))


@register(2015, 6, 2)
def part2(input_data):
    
    light_grid = {}
    brightness = 0

    for section in input_data.splitlines():

        matches = re.search(r"^(?P<switch>turn (on|off)|toggle) (?P<x1>[0-9]{1,3}),(?P<y1>[0-9]{1,3}) through (?P<x2>[0-9]{1,3}),(?P<y2>[0-9]{1,3})$", section)

        toggle = True if matches.group("switch") == "toggle" else False
        turn_on = True if matches.group("switch") == "turn on" else False

        x1_coordinate = int(matches.group("x1"))
        x2_coordinate = int(matches.group("x2"))
        y1_coordinate = int(matches.group("y1"))
        y2_coordinate = int(matches.group("y2"))


        for i in range(x1_coordinate, x2_coordinate+1):
            for j in range(y1_coordinate, y2_coordinate+1):

                position = f"{i}.{j}"

                if not position in light_grid:
                    light_grid[position] = 0
                
                if turn_on:
                    light_grid[position] = light_grid[position]+1
                    brightness += 1
                    continue

                if toggle:
                    light_grid[position] = light_grid[position]+2
                    brightness += 2
                    continue

                if light_grid[position] == 0:
                    continue

                light_grid[position] = light_grid[position]-1
                brightness -= 1

    return str(brightness)