from collections import defaultdict

# Register all solutions
puzzles = defaultdict(lambda: defaultdict(lambda: defaultdict(any)))

def register(year, day, part):
    def decorator(func):
        puzzles[year][day][part] = func
        return func
    return decorator
