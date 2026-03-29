from aoc.puzzles import register

@register(2015, 2, 1)
def part1(input_data):
    
    total_area = 0
    for box in input_data.splitlines():

        # Create a list with dimensions
        dimensions = [int(i) for i in box.split("x")]

        # Calculate area and sort it so smallest side is first
        areas = [dimensions[0]*dimensions[1], dimensions[1]*dimensions[2], dimensions[2]*dimensions[0]]
        areas.sort()

        # Add box area to total area
        total_area += areas[0] + sum([i * 2 for i in areas])
        
    return total_area


@register(2015, 2, 2)
def part2(input_data):
    
    total_ribbon = 0
    for box in input_data.splitlines():

        # Create a list with dimensions and sort it so smallest dimensions is first
        dimensions = [int(i) for i in box.split("x")]
        dimensions.sort()

        total_ribbon += dimensions[0]+dimensions[0]+dimensions[1]+dimensions[1]+(dimensions[0]*dimensions[1]*dimensions[2])
    
    return total_ribbon

