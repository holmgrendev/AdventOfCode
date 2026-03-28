from collections import defaultdict

# Register all solutions
puzzle_registry = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: lambda *args, **kwargs: None)))

def register(year, day, part):
    def decorator(func):
        puzzle_registry[year][day][part] = func
        return func
    return decorator