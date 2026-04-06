import time

from aoc.puzzles import register

container_amount = {}

@register(2015, 17, 1)
def part1(input_data):

    containers = []

    for line in input_data.splitlines():
        containers.append(int(line))

    containers.sort()
    
    return str(volume_check(0, containers, 150))
    

@register(2015, 17, 2)
def part2(input_data):

    global container_amount

    containers = []

    for line in input_data.splitlines():
        containers.append(int(line))

    containers.sort()

    container_check(0, 0, containers, 150)

    for _, amount in container_amount.items():
        if amount == 0:
            continue
        
        return amount
    

def container_check(current_volume, container_level, containers, max_volume):
    global container_amount

    container_level += 1

    if container_level not in container_amount:
        container_amount[container_level] = 0

    for i, container_volume in enumerate(containers):

        new_volume = current_volume + container_volume

        if new_volume == max_volume:
            container_amount[container_level] += 1
            continue

        if new_volume < max_volume:
            container_check(new_volume, container_level, containers[i+1:], max_volume)
        
        if new_volume > max_volume:
            break

def volume_check(current_volume, containers, max_volume):
    
    solutions = 0

    for i, container_volume in enumerate(containers):

        new_volume = current_volume + container_volume

        if new_volume == max_volume:
            solutions += 1
            continue

        if new_volume < max_volume:
            solutions += volume_check(new_volume, containers[i+1:], max_volume)
        
        if new_volume > max_volume:
            break
    
    return solutions
