from aoc.puzzles import register

@register(2015, 20, 1)
def part1(input_data):

    presents = int(input_data.strip())
    size = int((presents/10) + 1)
    houses = [0] * size
    found_house = 0
    
    for elf in range(1, size):
        for house in range(0, size, elf):
            houses[house] += elf*10

        if houses[elf] >= presents:
            found_house = elf
            break
            
    return found_house


@register(2015, 20, 2)
def part2(input_data):
    presents = int(input_data.strip())
    size = int((presents/10) + 1)
    houses = [0] * size
    found_house = 0
    
    for elf in range(1, size):
        deliveries = 0
        for house in range(0, size, elf):
            houses[house] += elf*11

            deliveries += 1
            if deliveries > 50:
                break

        if houses[elf] >= presents:
            found_house = elf
            break
            
    return found_house
