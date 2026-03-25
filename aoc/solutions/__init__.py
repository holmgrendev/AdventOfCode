import pkgutil, importlib

# Import every solution 
for _, puzzle, _ in pkgutil.walk_packages(__path__, prefix=__name__ + "."):
    importlib.import_module(puzzle)