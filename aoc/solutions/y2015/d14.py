import re

from aoc.puzzles import register

@register(2015, 14, 1)
def part1(input_data):

    competition_time = 2503
    statistics = {}

    for stats in input_data.splitlines():
        matches = re.search(r"^(?P<reindeer>.*) can fly (?P<speed>\d+) km\/s for (?P<time>\d+) seconds, but then must rest for (?P<rest>\d+) seconds.$", stats)

        statistics[matches.group("reindeer")] = {"speed": int(matches.group("speed")), "time": int(matches.group("time")), "rest": int(matches.group("rest"))}
    
    longest_distance = 0

    for _, reindeer in statistics.items():
        sequence = reindeer["time"] + reindeer["rest"]
        sequences = int(competition_time/sequence)

        if competition_time >= ((sequences*sequence) + reindeer["time"]):
            sequences += 1
            time_left = 0
        else:
            time_left = competition_time - (sequences*sequence)
        
        distance = sequences*(reindeer["speed"]*reindeer["time"]) +time_left*reindeer["speed"]

        if distance > longest_distance:
            longest_distance = distance
    
    return str(longest_distance)


@register(2015, 14, 2)
def part2(input_data):

    competition_time = 2503
    statistics = {}

    for stats in input_data.splitlines():
        matches = re.search(r"^(?P<reindeer>.*) can fly (?P<speed>\d+) km\/s for (?P<time>\d+) seconds, but then must rest for (?P<rest>\d+) seconds.$", stats)

        statistics[matches.group("reindeer")] = {"speed": int(matches.group("speed")), "time": int(matches.group("time")), "rest": int(matches.group("rest")), "points": 0}
    

    for i in range(1, competition_time+1):

        reindeer_distance = {}
        longest_distance = 0

        for reindeer, reindeer_statistic in statistics.items():
            reindeer_distance[reindeer] = reindeer_position(reindeer_statistic, i)

            if reindeer_distance[reindeer] > longest_distance:
                longest_distance = reindeer_distance[reindeer]
        
        for reindeer, distance in reindeer_distance.items():
            if distance == longest_distance:
                statistics[reindeer]["points"] += 1
    
    highest_point = 0
    for _, reindeer in statistics.items():
        if reindeer["points"] > highest_point:
            highest_point = reindeer["points"]
    
    return highest_point

        
def reindeer_position(reindeer, time):
    sequence = reindeer["time"] + reindeer["rest"]
    sequences = int(time/sequence)

    if time >= ((sequences*sequence) + reindeer["time"]):
        sequences += 1
        time_left = 0
    else:
        time_left = time - (sequences*sequence)
    
    return sequences*(reindeer["speed"]*reindeer["time"]) +time_left*reindeer["speed"]