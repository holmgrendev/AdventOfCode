from . import puzzle_registry, data
import aoc.solutions

def solve(year, day, part) -> (bool, str, str):

    check, input_data, error = data.get(year, day)
    if not check:
        return False, "", error
    
    if not year in puzzle_registry or not day in puzzle_registry[year] or not part in puzzle_registry[year][day]:
        return False, "", "Could not find selected puzzle."

    solution = puzzle_registry[year][day][part](input_data)

    if solution == "":
        return False, "", "Error solving puzzle."
    
    return True, solution, ""
    # send data to "the" solution 

def get_latest() -> (int, int, int):
    """
    Solve latest puzzle

    Returns:
        int: Returns year.
        int: Returns day.
        int: Returns part.
    """

    year = next(reversed(puzzle_registry))
    day = next(reversed(puzzle_registry[year]))
    part = next(reversed(puzzle_registry[year][day]))

    return year, day, part