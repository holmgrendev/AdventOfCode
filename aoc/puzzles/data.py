from pathlib import Path
from urllib import request
from aoc.config import config

def get(year, day) -> (bool, str, str):
    """
    Get puzzle input for a given year and day.

    Args:
        year (int): Puzzle year.
        day (int): Puzzle day.
    
    Returns:
        bool: Returns True if success while fetching input data.
        str: Puzzle input.
        str: Error message if any.
    """

    # Download file
    check, file_path, error = download(year, day)

    if not check:
        return False, "", error
    
    # Read file with data
    content = ""

    try:
        with open(file_path, "r") as file:
            while True:
                chunk = file.read(8192)

                if not chunk:
                    break

                content += chunk
    
    except Exception as e:
        return False, "", str(e)

    return True, content, ""

def download(year, day) -> (bool, Path(), str):
    """
    Check if puzzle input exists for a given year and day.
    Downloads it if it does not exists.

    Args:
        year (int): Puzzle year.
        day (int): Puzzle day.
    
    Returns:
        bool: Returns True if success while downloading or finding file.
        Path(): Path object to file.
        str: Error message if any.
    """
    
    downloads = Path.cwd() / config.get("input", "directory")

    # Check if download directory exist, create if not
    try:
        downloads.mkdir(exist_ok=True)

    except Exception as e:
        return False, Path(), str(e)
    
    # Determine url and file path
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    file_path = downloads / f"{year}{day}{config.get("input", "extension")}"

    # Check if file already exists
    if file_path.is_file():
        return True, file_path, ""

    # Prepare downloading
    req = request.Request(url)
    req.add_header("Cookie", f"session={config.get("input", "cookie")}")
    
    # Try downloading
    try:
        with request.urlopen(req) as response, open(file_path, "wb") as file:
            while True:
                chunk = response.read(8192)

                if not chunk:
                    break

                file.write(chunk)

    except Exception as e:
        return False, Path(), str(e)

    return True, file_path, ""
