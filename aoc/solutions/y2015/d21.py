import copy

from aoc.puzzles import register

enemy = {}
player = {"Hit Points": 100, "Damage": 0, "Armor": 0}

shop = {
    "Weapons": {
        "Dagger":       (8,   4,   0),
        "Shortsword":   (10,  5,   0),
        "Warhammer":    (25,  6,   0),
        "Longsword":    (40,  7,   0),
        "Greataxe":     (74,  8,   0)
    },

    "Armor":{
        "Leather":      (13,  0,   1),
        "Chainmail":    (31,  0,   2),
        "Splintmail":   (53,  0,   3),
        "Bandedmail":   (75,  0,   4),
        "Platemail":    (102, 0,   5)
    },

    "Rings":{
        "Damage +1":    (25,  1,   0),
        "Damage +2":    (50,  2,   0),
        "Damage +3":    (100, 3,   0),
        "Defense +1":   (20,  0,   1),
        "Defense +2":   (40,  0,   2),
        "Defense +3":   (80,  0,   3)
    }
}

@register(2015, 21, 1)
def part1(input_data):
    global enemy

    for statistics in input_data.splitlines():
        key, value = statistics.strip().split(": ", 1)
        enemy[key] = int(value)
    
    return claculate_winning_fight()

@register(2015, 21, 2)
def part2(input_data):
    global enemy

    for statistics in input_data.splitlines():
        key, value = statistics.strip().split(": ", 1)
        enemy[key] = int(value)
    
    return claculate_losing_fight()
      

def claculate_losing_fight():
    global enemy
    global player
    global shop

    highest_cost = 0
    
    for _, weapon in shop["Weapons"].items():
        cost = weapon[0]
        player["Damage"] = weapon[1]
        player["Armor"] = 0

        # Check if you can defeat the enemy using only weapon
        if not fight_enemy(player, enemy) and cost > highest_cost:
            highest_cost = cost
        
        for _, armor in shop["Armor"].items():
            cost = weapon[0] + armor[0]
            player["Armor"] = armor[2]

            # Check if you can fight with adding armor
            if not fight_enemy(player, enemy) and cost > highest_cost:
                highest_cost = cost
            
            for ring_key_1, ring_1 in shop["Rings"].items():
                cost = weapon[0] + armor[0] + ring_1[0]
                player["Damage"] = weapon[1] + ring_1[1]
                player["Armor"] = armor[2] + ring_1[2]

                # Check if you can fight with adding only one ring
                if not fight_enemy(player, enemy) and cost > highest_cost:
                    highest_cost = cost
                
                for ring_key_2, ring_2 in shop["Rings"].items():

                    if ring_key_1 == ring_key_2:
                        continue

                    cost = weapon[0] + armor[0] + ring_1[0] + ring_2[0]
                    player["Damage"] = weapon[1] + ring_1[1] + ring_2[1]
                    player["Armor"] = armor[2] + ring_1[2] + ring_2[2]

                    # Check if you can fight with adding another ring
                    if not fight_enemy(player, enemy) and cost > highest_cost:
                        highest_cost = cost
            

        for ring_key_1, ring_1 in shop["Rings"].items():
            cost = weapon[0] + ring_1[0]
            player["Damage"] = weapon[1] + ring_1[1]
            player["Armor"] = ring_1[2]

            # Check if you can fight with adding only one ring
            if not fight_enemy(player, enemy) and cost > highest_cost:
                highest_cost = cost
            
            for ring_key_2, ring_2 in shop["Rings"].items():

                if ring_key_1 == ring_key_2:
                    continue

                cost = weapon[0] + ring_1[0] + ring_2[0]
                player["Damage"] = weapon[1] + ring_1[1] + ring_2[1]
                player["Armor"] = ring_1[2] + ring_2[2]

                # Check if you can fight with adding another ring
                if not fight_enemy(player, enemy) and cost > highest_cost:
                    highest_cost = cost
    

    return str(highest_cost)


def claculate_winning_fight():
    global enemy
    global player
    global shop

    lowest_cost = 1000000
    
    for _, weapon in shop["Weapons"].items():
        cost = weapon[0]
        player["Damage"] = weapon[1]
        player["Armor"] = 0

        # Check if you can defeat the enemy using only weapon
        if fight_enemy(player, enemy) and cost < lowest_cost:
            lowest_cost = cost
        
        for _, armor in shop["Armor"].items():
            cost = weapon[0] + armor[0]
            player["Armor"] = armor[2]

            # Check if you can fight with adding armor
            if fight_enemy(player, enemy) and cost < lowest_cost:
                lowest_cost = cost
            
            for ring_key_1, ring_1 in shop["Rings"].items():
                cost = weapon[0] + armor[0] + ring_1[0]
                player["Damage"] = weapon[1] + ring_1[1]
                player["Armor"] = armor[2] + ring_1[2]

                # Check if you can fight with adding only one ring
                if fight_enemy(player, enemy) and cost < lowest_cost:
                    lowest_cost = cost
                
                for ring_key_2, ring_2 in shop["Rings"].items():

                    if ring_key_1 == ring_key_2:
                        continue

                    cost = weapon[0] + armor[0] + ring_1[0] + ring_2[0]
                    player["Damage"] = weapon[1] + ring_1[1] + ring_2[1]
                    player["Armor"] = armor[2] + ring_1[2] + ring_2[2]

                    # Check if you can fight with adding another ring
                    if fight_enemy(player, enemy) and cost < lowest_cost:
                        lowest_cost = cost
            

        for ring_key_1, ring_1 in shop["Rings"].items():
            cost = weapon[0] + ring_1[0]
            player["Damage"] = weapon[1] + ring_1[1]
            player["Armor"] = ring_1[2]

            # Check if you can fight with adding only one ring
            if fight_enemy(player, enemy) and cost < lowest_cost:
                lowest_cost = cost
            
            for ring_key_2, ring_2 in shop["Rings"].items():

                if ring_key_1 == ring_key_2:
                    continue

                cost = weapon[0] + ring_1[0] + ring_2[0]
                player["Damage"] = weapon[1] + ring_1[1] + ring_2[1]
                player["Armor"] = ring_1[2] + ring_2[2]

                # Check if you can fight with adding another ring
                if fight_enemy(player, enemy) and cost < lowest_cost:
                    lowest_cost = cost
    

    return str(lowest_cost)


def fight_enemy(player, enemy):

    player_attack = player["Damage"] - enemy["Armor"] if player["Damage"] > enemy["Armor"] else 1
    enemy_attack = enemy["Damage"] - player["Armor"] if enemy["Damage"] > player["Armor"] else 1
    
    if player_attack >= enemy_attack:
        return True
    
    return False

    