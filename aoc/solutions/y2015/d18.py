import copy

from aoc.puzzles import register

@register(2015, 18, 1)
def part1(input_data):

    # Create a light matrix
    light_matrix = {}
    for y, line in enumerate(input_data.splitlines()):
        for x, char in enumerate(line):
            coordinate = f"{x},{y}"
            light_matrix[coordinate] = {"x": x, "y": y, "state": True if char == "#" else False}


    # Initialize helpers for next step matrix
    light_matrix_next = copy.deepcopy(light_matrix)

    neighbor_coordinates = [
        {"x": -1, "y": -1},
        {"x": -1, "y": 0},
        {"x": -1, "y": 1},
        {"x": 0, "y": -1},
        {"x": 0, "y": 1},
        {"x": 1, "y": -1},
        {"x": 1, "y": 0},
        {"x": 1, "y": 1},
    ]

    matrix_boundary = {
        "min_x": 0,
        "max_x": 99,
        "min_y": 0,
        "max_y": 99,
    }
    


    for _ in range(100):
        active_lights = 0

        for coordinate, light in light_matrix.items():
            
            active_neighbors = 0

            # Check neighbors state
            for neighbor in neighbor_coordinates:

                neighbor_coordinate = {"x": light["x"] + neighbor["x"], "y": light["y"] + neighbor["y"]}
                
                if (
                    not (matrix_boundary["min_x"] <= neighbor_coordinate["x"] <= matrix_boundary["max_x"])
                    or not (matrix_boundary["min_y"] <= neighbor_coordinate["y"] <= matrix_boundary["max_y"])
                ):
                    continue

                if light_matrix[f"{neighbor_coordinate["x"]},{neighbor_coordinate["y"]}"]["state"]:
                    active_neighbors += 1
                
                if active_neighbors > 3:
                    break
            
            new_state = False

            if active_neighbors == 3:
                new_state = True
                active_lights += 1

            if active_neighbors == 2 and light["state"]:
                new_state = True
                active_lights += 1

            light_matrix_next[coordinate]["state"] = new_state

        light_matrix = copy.deepcopy(light_matrix_next)
    
    return active_lights


@register(2015, 18, 2)
def part2(input_data):

    # Create a light matrix
    light_matrix = {}
    for y, line in enumerate(input_data.splitlines()):
        for x, char in enumerate(line):
            coordinate = f"{x},{y}"
            light_matrix[coordinate] = {"x": x, "y": y, "state": True if char == "#" else False}


    # Initialize helpers for next step matrix
    light_matrix_next = copy.deepcopy(light_matrix)

    neighbor_coordinates = [
        {"x": -1, "y": -1},
        {"x": -1, "y": 0},
        {"x": -1, "y": 1},
        {"x": 0, "y": -1},
        {"x": 0, "y": 1},
        {"x": 1, "y": -1},
        {"x": 1, "y": 0},
        {"x": 1, "y": 1},
    ]

    matrix_boundary = {
        "min_x": 0,
        "max_x": 99,
        "min_y": 0,
        "max_y": 99,
    }

    stuck_lights = {
        f"{matrix_boundary["min_x"]},{matrix_boundary["min_y"]}": {"x": matrix_boundary["min_x"], "y": matrix_boundary["min_y"], "state": True},
        f"{matrix_boundary["max_x"]},{matrix_boundary["min_y"]}": {"x": matrix_boundary["max_x"], "y": matrix_boundary["min_y"], "state": True},
        f"{matrix_boundary["min_x"]},{matrix_boundary["max_y"]}": {"x": matrix_boundary["min_x"], "y": matrix_boundary["max_y"], "state": True},
        f"{matrix_boundary["max_x"]},{matrix_boundary["max_y"]}": {"x": matrix_boundary["max_x"], "y": matrix_boundary["max_y"], "state": True},
    }

    # Set stuck lights to active
    for coordinate, light in stuck_lights.items():
        light_matrix[coordinate] = light

    for _ in range(100):

        active_lights = 0

        for coordinate, light in light_matrix.items():
            
            active_neighbors = 0

            # Check neighbors state
            for neighbor in neighbor_coordinates:

                neighbor_coordinate = {"x": light["x"] + neighbor["x"], "y": light["y"] + neighbor["y"]}
                
                if (
                    not (matrix_boundary["min_x"] <= neighbor_coordinate["x"] <= matrix_boundary["max_x"])
                    or not (matrix_boundary["min_y"] <= neighbor_coordinate["y"] <= matrix_boundary["max_y"])
                ):
                    continue

                if light_matrix[f"{neighbor_coordinate["x"]},{neighbor_coordinate["y"]}"]["state"]:
                    active_neighbors += 1
                
                if active_neighbors > 3:
                    break
            
            new_state = False

            if coordinate in stuck_lights:
                new_state = True
                active_lights += 1

            elif active_neighbors == 3:
                new_state = True
                active_lights += 1

            elif active_neighbors == 2 and light["state"]:
                new_state = True
                active_lights += 1

            light_matrix_next[coordinate]["state"] = new_state

        light_matrix = copy.deepcopy(light_matrix_next)
    
    return active_lights