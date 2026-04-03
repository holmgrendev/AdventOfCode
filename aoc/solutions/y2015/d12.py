import re, json

from aoc.puzzles import register

@register(2015, 12, 1)
def part1(input_data):
    pattern = re.compile(r"\d+|-\d+")
    total = 0

    for number in pattern.finditer(input_data):
        total += int(number.group())
    
    return total
        

@register(2015, 12, 2)
def part2(input_data):
    json_data = json.dumps(check_json(json.loads(input_data)))

    pattern = re.compile(r"\d+|-\d+")
    total = 0

    for number in pattern.finditer(json_data):
        total += int(number.group())
    
    return total


def check_json(json_data):

    return_json_data = None

    if isinstance(json_data, list):
        return_json_data = json_data.copy()

        for i, item in enumerate(json_data):
            new_json_data = check_json(item)

            if new_json_data is False:
                return_json_data[i] = item
            else:
                return_json_data[i] = new_json_data
    
    
    elif isinstance(json_data, dict):
        return_json_data = json_data.copy()

        for key, value in json_data.items():
            new_json_data = check_json(value)

            if new_json_data is False:
                return_json_data = ""
                break
            else:
                return_json_data[key] = new_json_data

    else:
        if json_data == "red":
            return False
        
        return_json_data = json_data
    
    return return_json_data