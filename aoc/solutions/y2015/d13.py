import re

from aoc.puzzles import register

happiness_table = {}
initial_person = ""
persons = []

@register(2015, 13, 1)
def part1(input_data):
    return calculate(input_data, False)

@register(2015, 13, 2)
def part2(input_data):
    return calculate(input_data, True)


def calculate(input_data, myself):
    global happiness_table
    global persons
    global initial_person

    # Create happiness and person table
    for seating in input_data.splitlines():
        matches = re.search(r"^(?P<person_1>[A-Za-z]+) would (?P<mood>lose|gain) (?P<points>\d+).* (?P<person_2>[A-Za-z]+).$", seating)

        person_1 = matches.group("person_1")
        person_2 = matches.group("person_2")

        mood = 1 if matches.group("mood") == "gain" else -1

        happiness_table[f'{person_1}-{person_2}'] = mood*int(matches.group("points"))

        if person_1 not in persons:
            persons.append(person_1)

        if person_2 not in persons:
            persons.append(person_2)
    
    if myself:
        myself = "Host"

        for person in persons:
            happiness_table[f'{myself}-{person}'] = happiness_table[f'{person}-{myself}'] =0
        
        persons.append(myself)

    initial_person = persons.pop(0)

    happiness = calculate_happiness(initial_person, persons)
    return happiness["_total"]


def calculate_happiness(current_person, available_persons):
 
    global initial_person
    return_table = []

    if len(available_persons) == 0:
        return {current_person: happiness_table[f"{current_person}-{initial_person}"] + happiness_table[f"{initial_person}-{current_person}"], "_total": happiness_table[f"{current_person}-{initial_person}"] + happiness_table[f"{initial_person}-{current_person}"]}

    for person in available_persons:
        happiness_chart = {current_person: happiness_table[f"{current_person}-{person}"] +  happiness_table[f"{person}-{current_person}"]} | calculate_happiness(person, [x for x in available_persons if x != person])
        happiness_chart["_total"] += happiness_chart[current_person]
   
        if not return_table:
            return_table = happiness_chart
        
        if return_table["_total"] < happiness_chart["_total"]:
            return_table = happiness_chart
        
    return return_table