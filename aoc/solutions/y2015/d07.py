import re

from aoc.puzzles import register

@register(2015, 7, 1)
def part1(input_data):

    wires = {}
    operations = input_data.splitlines()

    # Iterate trough all lines until everything is solved
    while len(operations) > 0:

        # Iterate trough the current list
        for operation in operations:
            matches = re.search(r"^(?:(?P<wire_1>[a-z0-9]+) )?(?:(?P<gate>OR|AND|RSHIFT|LSHIFT|NOT) )?(?P<wire_2>[a-z0-9]+) -> (?P<output>[a-z]+)$", operation)

            # Check wire 2
            check, wire_2 = is_int(matches.group("wire_2"))

            if check:
                wire_2_value = int(wire_2)
            elif wire_2 in wires:
                wire_2_value = wires[wire_2]
            else:
                continue


            # Check wire 1
            check, wire_1 = is_int(matches.group("wire_1"))
            output = matches.group("output")
            gate = matches.group("gate")


            # Add value from value 2 if 1 is non-existent
            if not wire_1:
                if gate == None:
                    wires[output] = wire_2_value
                    operations.remove(operation)
                    continue
                
                wires[output] = 65535-wire_2_value
                operations.remove(operation)
                continue

            # Check and get values for wire 1 if found
            if check:
                wire_1_value = int(wire_1)
            elif wire_1 in wires:
                wire_1_value = wires[wire_1]
            else:
                continue

            # Do the bitwise operations
            match gate:
                case "OR":
                    wires[output] = wire_1_value | wire_2_value
                case "AND":
                    wires[output] = wire_1_value & wire_2_value
                case "RSHIFT":
                    wires[output] = wire_1_value >> wire_2_value
                case "LSHIFT":
                    wires[output] = wire_1_value << wire_2_value

            
            operations.remove(operation)

    return wires["a"]


@register(2015, 7, 2)
def part2(input_data):
    wires = {}
    operations = input_data.splitlines()

    # Tamper data
    # Get the new b-value
    b_value = part1(input_data)
    
    # Find b and remove it
    for operation in operations:
        if bool(re.match(r"^(.*) -> b$", operation)):
            operations.remove(operation)
    
    # Add the new b
    operations.append(f"{b_value} -> b")

    # Iterate trough all lines until everything is solved
    while len(operations) > 0:

        # Iterate trough the current list
        for operation in operations:
            matches = re.search(r"^(?:(?P<wire_1>[a-z0-9]+) )?(?:(?P<gate>OR|AND|RSHIFT|LSHIFT|NOT) )?(?P<wire_2>[a-z0-9]+) -> (?P<output>[a-z]+)$", operation)

            # Check wire 2
            check, wire_2 = is_int(matches.group("wire_2"))

            if check:
                wire_2_value = int(wire_2)
            elif wire_2 in wires:
                wire_2_value = wires[wire_2]
            else:
                continue


            # Check wire 1
            check, wire_1 = is_int(matches.group("wire_1"))
            output = matches.group("output")
            gate = matches.group("gate")


            # Add value from value 2 if 1 is non-existent
            if not wire_1:
                if gate == None:
                    wires[output] = wire_2_value
                    operations.remove(operation)
                    continue
                
                wires[output] = 65535-wire_2_value
                operations.remove(operation)
                continue

            # Check and get values for wire 1 if found
            if check:
                wire_1_value = int(wire_1)
            elif wire_1 in wires:
                wire_1_value = wires[wire_1]
            else:
                continue

            # Do the bitwise operations
            match gate:
                case "OR":
                    wires[output] = wire_1_value | wire_2_value
                case "AND":
                    wires[output] = wire_1_value & wire_2_value
                case "RSHIFT":
                    wires[output] = wire_1_value >> wire_2_value
                case "LSHIFT":
                    wires[output] = wire_1_value << wire_2_value

            
            operations.remove(operation)

    return wires["a"]



def is_int(value) -> (bool, str):

    if value == None:
        return False, ""

    try:
        int(value)
        return True, value
    except Exception:
        return False, value