import re

from aoc.puzzles import register

@register(2015, 15, 1)
def part1(input_data):

    ingredients = {}

    for line in input_data.splitlines():
        matches = re.search(r"^(?P<ingredient>.*): capacity (?P<capacity>\d+|-\d+), durability (?P<durability>\d+|-\d+), flavor (?P<flavor>\d+|-\d+), texture (?P<texture>\d+|-\d+), calories (?P<calories>\d+|-\d+)$", line)

        ingredients[matches.group("ingredient")] = {"capacity": int(matches.group("capacity")), "durability": int(matches.group("durability")), "flavor": int(matches.group("flavor")), "texture": int(matches.group("texture")), "calories": int(matches.group("calories"))}
    
    highest_score = 0

    for fro_tbsp in range(1, 101):
        for can_tbsp in range(1, 101 - fro_tbsp):
            for but_tbsp in range(1, 101 - fro_tbsp - can_tbsp):
                sug_tbsp = 100 - fro_tbsp - can_tbsp - but_tbsp

                ingr_tbsp = {"Frosting": fro_tbsp, "Candy": can_tbsp, "Butterscotch": but_tbsp, "Sugar": sug_tbsp}
                total = {"capacity": 0, "durability": 0, "flavor": 0, "texture": 0}

                for ingr, tbsp in ingr_tbsp.items():
                    for prop, _ in total.items():
                        total[prop] += ingredients[ingr][prop]*tbsp
                
                if total["capacity"] <= 0 or total["durability"] <= 0 or total["flavor"] <= 0 or total["texture"] <= 0:
                    continue

                total_score = 1
                for _, score in total.items():
                    total_score *= score

                if total_score > highest_score:
                    highest_score = total_score

    return str(highest_score)


@register(2015, 15, 2)
def part2(input_data):

    ingredients = {}

    for line in input_data.splitlines():
        matches = re.search(r"^(?P<ingredient>.*): capacity (?P<capacity>\d+|-\d+), durability (?P<durability>\d+|-\d+), flavor (?P<flavor>\d+|-\d+), texture (?P<texture>\d+|-\d+), calories (?P<calories>\d+|-\d+)$", line)

        ingredients[matches.group("ingredient")] = {"capacity": int(matches.group("capacity")), "durability": int(matches.group("durability")), "flavor": int(matches.group("flavor")), "texture": int(matches.group("texture")), "calories": int(matches.group("calories"))}
    
    highest_score = 0

    for fro_tbsp in range(1, 101):
        for can_tbsp in range(1, 101 - fro_tbsp):
            for but_tbsp in range(1, 101 - fro_tbsp - can_tbsp):
                sug_tbsp = 100 - fro_tbsp - can_tbsp - but_tbsp

                ingr_tbsp = {"Frosting": fro_tbsp, "Candy": can_tbsp, "Butterscotch": but_tbsp, "Sugar": sug_tbsp}
                total = {"capacity": 0, "durability": 0, "flavor": 0, "texture": 0}

                calories = 0

                for ingr, tbsp in ingr_tbsp.items():
                    calories += ingredients[ingr]["calories"]*tbsp
                    for prop, _ in total.items():
                        total[prop] += ingredients[ingr][prop]*tbsp
                
                if total["capacity"] <= 0 or total["durability"] <= 0 or total["flavor"] <= 0 or total["texture"] <= 0:
                    continue

                if calories != 500:
                    continue

                total_score = 1
                for _, score in total.items():
                    total_score *= score

                if total_score > highest_score:
                    highest_score = total_score

    return str(highest_score)
