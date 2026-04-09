import re

from aoc.puzzles import register

@register(2015, 19, 1)
def part1(input_data):

    replacements = []
    molecule = ""
    molecules = []

    for line in input_data.splitlines():
        if line == "":
            continue

        matches = re.search(r"^(?P<element>\w+) => (?P<molecule>\w+)$", line)

        if not matches:
            molecule = line.strip()
            continue

        replacements.append([matches.group("element"), matches.group("molecule")])
    
    for replacement in replacements:
        for match in re.finditer(re.escape(replacement[0]), molecule):
            start, end = match.span()
            new_molecule = molecule[:start] + replacement[1] + molecule[end:]

            if not new_molecule in molecules:
                molecules.append(new_molecule)
    
    return str(len(molecules))




@register(2015, 19, 2)
def part2(input_data):
    return "No solution exists yet"