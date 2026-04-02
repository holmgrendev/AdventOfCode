import re

from aoc.puzzles import register

route_distances = {}
initial_destination = ""
destinations = []

@register(2015, 9, 1)
def part1(input_data):
    return calculate(input_data, True)


@register(2015, 9, 2)
def part1(input_data):
    return calculate(input_data, False)


def calculate(input_data, shortest):
    global destinations
    global initial_destination

    # Create route table
    for route in input_data.splitlines():
        matches = re.search(r"^(?P<location_1>[A-Za-z]+) to (?P<location_2>[A-Za-z]+) = (?P<distance>[0-9]+)$", route)

        location_1 = matches.group("location_1")
        location_2 = matches.group("location_2")

        route_distances[f'{location_1}-{location_2}'] = route_distances[f'{location_2}-{location_1}'] = int(matches.group("distance"))

        if location_1 not in destinations:
            destinations.append(location_1)

        if location_2 not in destinations:
            destinations.append(location_2)

    # Go trough routes and create round trips
    round_trips = []
    initial_destination = destinations.pop(0)

    for destination in destinations:
        distance_table = {
            initial_destination: route_distances[f"{initial_destination}-{destination}"]
            } | \
            calculate_distance(destination, [x for x in destinations if x != destination], shortest)
        
        distance_table["_total"] += distance_table[initial_destination]

        round_trips.append(distance_table.copy())

    # Remove the desired distance in round trips
    result = 0

    for round_trip in round_trips:
        saved_distance = 0

        for destination, distance in round_trip.items():
            if destination == "_total":
                continue

            if shortest and saved_distance != 0 and distance < saved_distance:
                continue

            if not shortest and saved_distance != 0 and distance > saved_distance:
                continue

            saved_distance = distance

        round_trip["_total"] -= saved_distance

        if result == 0:
            result = round_trip["_total"]
        
        if shortest and round_trip["_total"] < result:
            result = round_trip["_total"]
        
        if not shortest and round_trip["_total"] > result:
            result = round_trip["_total"]

    return result


def calculate_distance(current_destination, available_destinations, shortest):
 
    global initial_destination
    return_table = []

    if len(available_destinations) == 0:
        return {current_destination: route_distances[f"{current_destination}-{initial_destination}"], "_total": route_distances[f"{current_destination}-{initial_destination}"]}

    for destination in available_destinations:
        distance_table = {current_destination: route_distances[f"{current_destination}-{destination}"]} | calculate_distance(destination, [x for x in available_destinations if x != destination], shortest)
        distance_table["_total"] += distance_table[current_destination]
   
        if not return_table:
            return_table = distance_table
        
        if shortest and return_table["_total"] > distance_table["_total"]:
            return_table = distance_table

        if not shortest and return_table["_total"] < distance_table["_total"]:
            return_table = distance_table
        
    return return_table