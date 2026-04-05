import re

from aoc.puzzles import register

@register(2015, 16, 1)
def part1(input_data):

    aunt_property = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}
    aunts = {}

    for line in input_data.splitlines():
        aunts[re.findall(r"^Sue (\d+)", line)[0]] = dict(re.findall(r"([a-z]+): ([0-9]+)", line))
    
    aunt_list = aunts.copy()

    for prop, count in aunt_property.items():
        for aunt, props in aunts.items():
            if prop not in props or aunt not in aunt_list:
                continue

            if int(props[prop]) != count:
                del aunt_list[aunt]
    
            if len(aunt_list) <= 1:
                break

        if len(aunt_list) <= 1:
            break

    
    return next(iter(aunt_list))

@register(2015, 16, 2)
def part2(input_data):

    aunt_property = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}
    aunts = {}

    for line in input_data.splitlines():
        aunts[re.findall(r"^Sue (\d+)", line)[0]] = dict(re.findall(r"([a-z]+): ([0-9]+)", line))
    
    aunt_list = aunts.copy()

    for prop, count in aunt_property.items():
        for aunt, props in aunts.items():
            if prop not in props or aunt not in aunt_list:
                continue
            
            if prop == "cats" or prop == "trees":
                if int(props[prop]) <= count:
                    del aunt_list[aunt]

            elif prop == "pomeranians" or prop == "goldfish":
                if int(props[prop]) >= count:
                    del aunt_list[aunt]

            elif int(props[prop]) != count:
                del aunt_list[aunt]
    
            if len(aunt_list) <= 1:
                break

        if len(aunt_list) <= 1:
            break

    
    return next(iter(aunt_list))

