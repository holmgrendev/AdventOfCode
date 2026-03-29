from aoc.puzzles import register

@register(2015, 3, 1)
def part1(input_data):

    x_coordinate = 0
    y_coordinate = 0
    deliveries = 1
    tracker = ["0.0"]

    for c in input_data:

        match c:
            case "<":
                x_coordinate -= 1
            case ">":
                x_coordinate += 1
            case "^":
                y_coordinate += 1
            case "v":
                y_coordinate -= 1

        position = f"{x_coordinate}.{y_coordinate}"

        if not position in tracker:
            tracker.append(position)
            deliveries += 1
    
    return deliveries


@register(2015, 3, 2)
def part2(input_data):

    x_coordinate_santa = 0
    y_coordinate_santa = 0
    x_coordinate_robo_santa = 0
    y_coordinate_robo_santa = 0
    deliveries = 1
    tracker = ["0.0"]

    for i, c in enumerate(input_data):
        if i%2 == 0:
            x_coordinate = x_coordinate_santa
            y_coordinate = y_coordinate_santa
        else:
            x_coordinate = x_coordinate_robo_santa
            y_coordinate = y_coordinate_robo_santa

        match c:
            case "<":
                x_coordinate -= 1
            case ">":
                x_coordinate += 1
            case "^":
                y_coordinate += 1
            case "v":
                y_coordinate -= 1
        
        if i%2 == 0:
            x_coordinate_santa = x_coordinate
            y_coordinate_santa = y_coordinate
        else:
            x_coordinate_robo_santa = x_coordinate
            y_coordinate_robo_santa = y_coordinate

        position = f"{x_coordinate}.{y_coordinate}"

        if not position in tracker:
            tracker.append(position)
            deliveries += 1

    return deliveries
        

            
